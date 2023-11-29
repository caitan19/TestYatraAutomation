import time

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightsResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    LIST_OF_CITIES = "//div[@class='viewport']/div/div/li"
    DEPARTURE_DATE = "//input[@id='BE_flight_origin_date']"
    RETURN_DATE = "//input[@id='BE_flight_arrival_date']"
    LIST_OF_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    LIST_OF_RETURN_DATES = "//div[@id='monthWrapper']//tbody[@class='BE_flight_arrival_date']"
    SEARCH_FLIGHTS_BUTTON = "BE_flight_flsearch_btn"
    ROUND_TRIP_TAB = "//a[@title='Round Trip']"
    POPUP_AD_BOX = "//div[@id='webklipper-publisher-widget-container-notification-container']"

    # Methods to get the fields
    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getDepatureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPARTURE_DATE)

    def getReturnDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.RETURN_DATE)

    def getDepatureCitiesList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.LIST_OF_CITIES)

    def getDepatureDatesList(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LIST_OF_DATES)

    def getReturnDatesList(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LIST_OF_RETURN_DATES)

    def getSearchBtnField(self):
        return self.wait_until_element_is_clickable(By.ID, self.SEARCH_FLIGHTS_BUTTON)

    def getRoundTripTabField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ROUND_TRIP_TAB)

    def getPopup(self):
        return self.wait_for_presence_of_element(By.XPATH, self.POPUP_AD_BOX)

    # Methods to perform the tests
    def inputDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        #self.driver.execute_script("arguments[0].click()", source)
        time.sleep(2)
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def inputGoingToLocation(self, goinglocation):
        self.getGoingToField().click()
        #self.driver.execute_script("arguments[0].click()", destination)
        time.sleep(5)
        self.getGoingToField().send_keys(goinglocation)
        #self.getGoingToField().send_keys(Keys.ENTER)
        #time.sleep(2)
        listResults = self.getDepatureCitiesList()
        for result in listResults:
            self.log.debug("result text is {0}: ".format(result.text))
            self.log.debug("Location is {0}: ".format(goinglocation))
            if goinglocation in result.text:
                result.click()
                break

    def inputGoingToDate(self, traveldate):
        self.getDepatureDateField().click()
        #self.driver.execute_script("arguments[0].click()", depature_date)
        List_dates = self.getDepatureDatesList().find_elements(By.XPATH, self.LIST_OF_DATES)

        for date in List_dates:
            if date.get_attribute("data-date") == traveldate:
                date.click()
                time.sleep(2)
                # driver.execute_script("arguments[0].click();", date)
                break

    def inputReturnToDate(self, returndate):
        self.getReturnDateField().click()
        # self.driver.execute_script("arguments[0].click()", depature_date)
        List_dates = self.getReturnDatesList().find_elements(By.XPATH, self.LIST_OF_DATES)

        for date in List_dates:
            if date.get_attribute("data-date") == returndate:
                date.click()
                time.sleep(2)
                # driver.execute_script("arguments[0].click();", date)
                break

    def clickSearchBtn(self):
        search_btn = self.getSearchBtnField()
        search_btn.click()

    def clickRoundTripTab(self):
        round_trip_tab = self.getRoundTripTabField()
        round_trip_tab.click()

    def closePopupWin(self):
        '''popup = self.getPopup()
        self.log.debug(popup)'''
        time.sleep(30)
        self.close_popup()

    # Search flights method
    def SearchFlights(self, departlocation, goinglocation, traveldate):
        self.closePopupWin()
        self.inputDepartFromLocation(departlocation)
        self.inputGoingToLocation(goinglocation)
        self.inputGoingToDate(traveldate)
        self.clickSearchBtn()
        sf = SearchFlightsResults(self.driver)
        return sf

    def SearchRoundTripFlights(self, departlocation, goinglocation, traveldate, returndate):
        #self.closePopupWin()
        self.clickRoundTripTab()
        self.inputDepartFromLocation(departlocation)
        self.inputGoingToLocation(goinglocation)
        self.inputGoingToDate(traveldate)
        self.inputReturnToDate(returndate)
        self.clickSearchBtn()
        sf = SearchFlightsResults(self.driver)
        return sf

    '''def departfrom(self, departlocation):

        depart_from = self.wait_until_element_is_clickable(By.XPATH,
                                                           "//input[@id='BE_flight_origin_city']")  # driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys(departlocation)
        # time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        # time.sleep(3)'''

    '''def goingto(self, goinglocation):
        arival_to = self.wait_until_element_is_clickable(By.XPATH,
                                                         "//input[@id='BE_flight_arrival_city']")  # driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        arival_to.click()
        time.sleep(2)
        arival_to.send_keys(goinglocation)
        # arival_to.send_keys(Keys.ENTER)
        # time.sleep(4)
        listResults = self.wait_for_presence_of_all_elements(By.XPATH,
                                                             "//div[@class='viewport']/div/div/li")  # driver.find_elements(By.XPATH, "//div[@class='viewport']/div/div/li")
        for result in listResults:
            if "New York (JFK)" in result.text:
                result.click()
                break'''

    '''def selectdate(self, traveldate):
        # ewait = WebDriverWait(driver, 10)
        # fwait = WebDriverWait(driver, 10, 1,ignored_exceptions=[ElementClickInterceptedException])  # example of fluent wait
        od = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")
        od.click()
        # self.driver.execute_script("arguments[0].click()", od)
        allDates = self.wait_until_element_is_clickable(By.XPATH,
                                                        "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        List_dates = allDates.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for date in List_dates:
            if date.get_attribute("data-date") == traveldate:
                date.click()
                time.sleep(4)
                # driver.execute_script("arguments[0].click();", date)
                break'''

    '''def clicksearch(self):
        search_btn = self.wait_until_element_is_clickable(By.ID, "BE_flight_flsearch_btn")
        search_btn.click()'''
