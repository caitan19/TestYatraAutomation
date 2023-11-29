This project aims to automate few scenarios for the travel bookings site https://www.yatra.com/

The project uses the Page Object Model approach and as such the test data is stored separately in .json files. The locators reside in their respective page object to prevent additional file read overheads.

The test_searchOneStopFlights.py file contains 4 tests.

To run the tests navigate to the TestFrameworkDemo folder and run the following command: * pytest --browser chrome --html=reports/testReport.html -This will run all the testcases. --browser is a user-defined option and is defined in the conftest.py file. You can also run this on edge with --browser edge option. If no browser option is given, then by default the tests will run in chrome. * --html=reports/testReport.html -This will generate a basic html report after the tests are run and will create a testReport.html file under reports folder * You can also run a specific testcase using the folllowing command pytest -k "test_hotel_multiple_room" -v --browser chrome --html=reports/testReport.html * You can also run specific groups of testcases using the custom marker mention in the @pytest.mark decorator

Make sure to use Python 3.11.4 or higher

Other requirements are mentioned in the requirements.txt file
