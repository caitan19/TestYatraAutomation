import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from utilities.utils import Utils
import pytest_html


@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
    if browser == "chrome" or browser == None:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print("Invalid browser option")
    # ewait = WebDriverWait(driver, 30)
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    #driver.execute_script("location.reload(true);")
    '''driver.refresh()
    print("Browser refreshed successfully!")'''
    request.cls.driver = driver
    # request.cls.ewait = ewait
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True, scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_dir = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_dir, file_name)
            driver.save_screenshot(destinationFile)
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras

        '''
        This code defines two fixtures using the pytest testing framework. These fixtures are used to set up and manage a WebDriver instance for browser automation. Let's break down each part of the code:

1. **`@pytest.fixture(autouse=True)`**:
   - This decorator marks a function as a pytest fixture, and `autouse=True` indicates that this fixture should be automatically used by all test functions without explicitly requesting it as an argument.

2. **`def setup(request, browser):`**:
   - This is the implementation of the first fixture. It takes two parameters: `request` and `browser`. The `request` parameter is provided by pytest and contains information about the executing test, and `browser` is a custom parameter that the fixture expects.

3. **Browser Setup**:
   - The code checks the value of the `browser` parameter to determine which browser to use. It supports "chrome," "ff" (Firefox), "edge" (Edge), and a default case for an invalid browser option.
   - It then sets up a WebDriver instance accordingly using the appropriate driver (ChromeDriver, GeckoDriver for Firefox, EdgeDriver) downloaded and managed by WebDriverManager.

4. **Common Setup Actions**:
   - `driver.maximize_window()`: Maximizes the browser window.
   - `driver.get("https://www.yatra.com/")`: Navigates the browser to the specified URL.

5. **Fixture Teardown Actions**:
   - `request.cls.driver = driver`: Attaches the WebDriver instance to the test class, making it accessible in the test methods.
   - `yield`: This is the point where the actual test runs. The `yield` statement allows the test to run and continues execution after the test has completed.
   - `driver.quit()`: Quits the WebDriver session, closing the browser and releasing associated resources. This is performed after the test has run.

6. **`def pytest_addoption(parser):`**:
   - This function is a hook provided by pytest for adding command-line options. It is used here to add a `--browser` option, allowing the user to specify the browser for test execution.

7. **`@pytest.fixture(autouse=True, scope="class")`**:
   - This is the implementation of the second fixture named `browser`. It has `autouse=True`, meaning it will be automatically used by all test functions. The `scope="class"` parameter specifies that the fixture has class scope, meaning it will be set up and torn down once per test class.

8. **`return request.config.getoption("--browser")`**:
   - This fixture retrieves the value of the `--browser` command-line option using `request.config.getoption("--browser")`. It returns the specified browser value, which will be used by the first fixture to determine the browser for test execution.

In summary, these fixtures work together to set up and manage the WebDriver instance for browser automation, allowing users to specify the browser via a command-line option. The first fixture (`setup`) handles the actual browser setup and teardown, while the second fixture (`browser`) provides the browser value specified by the user.
        '''