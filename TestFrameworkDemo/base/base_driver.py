import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import Utils


class BaseDriver:
    log = Utils.custom_logger()

    def __init__(self, driver):
        self.driver = driver
        # self.ewait = WebDriverWait(driver, 30, ignored_exceptions=(StaleElementReferenceException,))

    IFRAME_POPUP = "//iframe[@id='webklipper-publisher-widget-container-notification-frame']"
    POPUP_CLOSE_BTN = "//i[@class='wewidgeticon we_close']"

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
        match = False
        while match == False:
            lastCount = pageLength
            time.sleep(4)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
            if lastCount == pageLength:
                match = True

        time.sleep(4)

    def close_popup(self):
        popup_iframe = self.wait_for_presence_of_element(By.XPATH, self.IFRAME_POPUP)
        self.log.debug(popup_iframe)
        self.driver.switch_to.frame(popup_iframe)
        close = self.wait_for_presence_of_element(By.XPATH, self.POPUP_CLOSE_BTN).find_element(By.XPATH, self.POPUP_CLOSE_BTN)
        self.driver.execute_script("arguments[0].click()", close)
        self.driver.switch_to.default_content()

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        # list_of_elements = None
        attempt = 1
        while True:
            try:
                ewait = WebDriverWait(self.driver, 50)
                list_of_elements = ewait.until(EC.presence_of_all_elements_located((locator_type, locator)))
                return list_of_elements
            except StaleElementReferenceException:
                # print("Exception occurred during waiting for all elements.")
                if attempt == 15:
                    raise
                attempt += 1

    def wait_until_element_is_clickable(self, locator_type, locator):
        # element = None
        attempt = 1
        while True:
            try:
                ewait = WebDriverWait(self.driver, 50)
                element = ewait.until(EC.element_to_be_clickable((locator_type, locator)))
                return element
            except StaleElementReferenceException:
                # print("Exception occurred during waiting for object to be clickable.")
                if attempt == 15:
                    raise
                attempt += 1

    def wait_for_presence_of_element(self, locator_type, locator):
        # element = None
        attempt = 1
        while True:
            try:
                ewait = WebDriverWait(self.driver, 50)
                element = ewait.until(EC.presence_of_element_located((locator_type, locator)))
                return element
            except StaleElementReferenceException:
                # print("Exception occurred during waiting for object to be clickable.")
                if attempt == 15:
                    raise
                attempt += 1
