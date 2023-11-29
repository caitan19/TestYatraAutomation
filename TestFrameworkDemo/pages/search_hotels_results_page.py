import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchHotelsResults(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    All_RATINGS_RESULTS_LIST = "//li[@class='pr hs-size-22 icon-pos-left-center fs-13 trip-color ng-scope']//span//span[contains(text(), '/5')]"
    FILTER_BY_1_AND_ABOVE_STARS_ICON = "//p[normalize-space()='1 +']"
    FILTER_BY_2_AND_ABOVE_STARS_ICON = "//p[normalize-space()='2 +']"
    FILTER_BY_3_AND_ABOVE_STARS_ICON = "//p[normalize-space()='3 +']"
    FILTER_BY_4_AND_ABOVE_STARS_ICON = "//p[normalize-space()='4 +']"
    FILTER_BY_5_AND_ABOVE_STARS_ICON = "//p[normalize-space()='5 +']"

    # Methods to get the fields
    def getAllRatingsIcon(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.All_RATINGS_RESULTS_LIST)

    def get1PlusStarsIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_1_AND_ABOVE_STARS_ICON)

    def get2PlusStarsIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_AND_ABOVE_STARS_ICON)
    def get3PlusStarsIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_3_AND_ABOVE_STARS_ICON)

    def get4PlusStarsIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_4_AND_ABOVE_STARS_ICON)

    def get5PlusStarsIcon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_5_AND_ABOVE_STARS_ICON)


    # Methods to perform the tests
    def filter_hotels(self, by_ratings):
        if by_ratings == "1+":
            one_plus_btn = self.get1PlusStarsIcon()
            one_plus_btn.click()
            self.log.debug("Selected hotels with 1 + ratings")
            time.sleep(4)
        elif by_ratings == "2+":
            two_plus_btn = self.get2PlusStarsIcon()
            two_plus_btn.click()
            self.log.debug("Selected hotels with 2 + ratings")
            time.sleep(4)
        elif by_ratings == "3+":
            three_plus_btn = self.get3PlusStarsIcon()
            three_plus_btn.click()
            self.log.debug("Selected hotels with 3 + ratings")
            time.sleep(4)
        elif by_ratings == "4+":
            four_plus_btn = self.get4PlusStarsIcon()
            four_plus_btn.click()
            self.log.debug("Selected hotels with 4 + ratings")
            time.sleep(4)
        elif by_ratings == "5+":
            five_plus_btn = self.get5PlusStarsIcon()
            five_plus_btn.click()
            self.log.debug("Selected hotels with 4 + ratings")
            time.sleep(4)
        else:
            self.log.debug("Please provide a valid input")
