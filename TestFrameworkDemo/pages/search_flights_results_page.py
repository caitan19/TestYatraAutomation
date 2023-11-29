import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightsResults(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FILTER_BY_0_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    SEARCH_FLIGHTS_RESULT_LIST = "//span[contains(text(), '1 Stop') or contains(text(), '2 Stops') or contains(text(), 'Non Stop')]"

    # Methods to get the fields
    def getNonStopIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_0_STOP_ICON)

    def getOneStopIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def getTwoStopIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def getSearchFlightsResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHTS_RESULT_LIST)

    # Methods to perform the tests
    def filter_flights(self, by_stop):
        if by_stop == "Non Stop":
            stop_btn = self.getNonStopIcon()
            stop_btn.click()
            self.log.debug("Selected flights with no stops")
            time.sleep(4)
        elif by_stop == "1 Stop":
            stop_btn = self.getOneStopIcon()
            stop_btn.click()
            self.log.debug("Selected flights with 1 stop")
            time.sleep(4)
        elif by_stop == "2 Stops":
            stop_btn = self.getTwoStopIcon()
            stop_btn.click()
            self.log.debug("Selected flights with 2 stops")
            time.sleep(4)
        else:
            self.log.debug("Please provide a valid input")
