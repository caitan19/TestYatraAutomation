import time

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightsResults
from selenium.webdriver.support.select import Select
from utilities.utils import Utils


class HotelSearchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CHECKIN_DATE_FIELD = "//input[@id='BE_hotel_checkin_date']"
    CHECKOUT_DATE_FIELD = "//input[@id='BE_hotel_checkout_date']"
    CHECKIN_DATE_LIST = "//tbody[@class='BE_hotel_checkin_date']//tr//td[@class!='inActiveTD']"
    CHECKOUT_DATE_LIST = "//tbody[@class='BE_hotel_checkout_date']//tr//td[@class!='inActiveTD']"
    TRAVELLER_AND_HOTEL_OX_FIELD = "//div[@id='BE_Hotel_pax_info']"
    ADD_ADULT_FIELD = "//div[@class='pax-limit clearfix w100 col-x-fluid fl'][1]//div[@class='ddTitle borderRadiusTp']/span[@class='ddSpinnerPlus']"
    SEARCH_HOTEL_BTN = "//input[@id='BE_hotel_htsearch_btn']"
    HOTEL_LOCATION = "//input[@id='BE_hotel_destination_city']"
    HOTELS_TAB_FIELD = "//a[@id='booking_engine_hotels']"
    ADD_ROOM_BUTTON_FIELD = "//a[normalize-space()='Add room']"
    ADD_CHILD_FIELD = "//div[@data-hotelroom='2']//div[@class='pax-limit clearfix w100 col-x-fluid fl'][2]//div[@class='ddTitle borderRadiusTp']/span[@class='ddSpinnerPlus']"
    AGE_DROP_DOWN_FIELD = "//select[@class='ageselect']"

    # Methods to get the fields
    def getCheckInField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHECKIN_DATE_FIELD)

    def getCheckOutField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHECKOUT_DATE_FIELD)

    def getTravellerHotelField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TRAVELLER_AND_HOTEL_OX_FIELD)

    def getAddAdultField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_ADULT_FIELD)

    def getAddChildField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_CHILD_FIELD)

    def getAgeDropDownField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.AGE_DROP_DOWN_FIELD)

    def getSearchHotelBtnField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_HOTEL_BTN)

    def getHotelLocationFeild(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.HOTEL_LOCATION)

    def getHotelTabField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.HOTELS_TAB_FIELD)

    def getCheckinDateList(self):
        return  self.wait_until_element_is_clickable(By.XPATH, self.CHECKIN_DATE_LIST)

    def getCheckoutDateList(self):
        return  self.wait_until_element_is_clickable(By.XPATH, self.CHECKOUT_DATE_LIST)

    def getAddRoomButtonField(self):
        return  self.wait_until_element_is_clickable(By.XPATH, self.ADD_ROOM_BUTTON_FIELD)

    # Methods to perform the tests
    def inputHotelLocation(self, location):
        source = self.getHotelLocationFeild().click()
        #self.driver.execute_script("arguments[0].click()", source)
        time.sleep(5)
        self.getHotelLocationFeild().send_keys(location)
        self.getHotelLocationFeild().send_keys(Keys.ENTER)

    def inscreaseNumberOfAdults(self):
        self.getAddAdultField().click()
        #self.driver.execute_script("arguments[0].click()", destination)
        time.sleep(5)

    def inputCheckinDate(self, checkindate):
        self.getCheckInField().click()
        #self.driver.execute_script("arguments[0].click()", depature_date)
        List_checkin_dates = self.getCheckinDateList().find_elements(By.XPATH, self.CHECKIN_DATE_LIST)

        for date in List_checkin_dates:
            if date.get_attribute("data-date") == checkindate:
                checkin_date = date #.click()
                self.driver.execute_script('arguments[0].click()', checkin_date)
                time.sleep(2)
                # driver.execute_script("arguments[0].click();", date)
                break

    def inputCheckoutDate(self, checkoutdate):
        self.getCheckOutField().click()
        # self.driver.execute_script("arguments[0].click()", depature_date)
        List_checkout_dates = self.getCheckoutDateList().find_elements(By.XPATH, self.CHECKOUT_DATE_LIST)

        for date in List_checkout_dates:
            if date.get_attribute("data-date") == checkoutdate:
                checkout_date = date#.click()
                self.driver.execute_script('arguments[0].click()', checkout_date)
                time.sleep(2)
                # driver.execute_script("arguments[0].click();", date)
                break

    def inputNewRoom(self):
        add_room_btn = self.getAddRoomButtonField()
        add_room_btn.click()

    def addChild(self):
        self.getAddChildField().click()
        age_dd = self.getAgeDropDownField().find_element(By.XPATH, self.AGE_DROP_DOWN_FIELD)
        dropdown = Select(age_dd)
        dropdown.select_by_visible_text("5")
        time.sleep(2)
    def clickSearchBtn(self):
        search_btn = self.getSearchHotelBtnField()
        search_btn.click()

    def clickTravellerAndHotelField(self):
        hnt_btn = self.getTravellerHotelField()
        hnt_btn.click()
    def clickHotelsTab(self):
        hotels_tab = self.getHotelTabField()
        hotels_tab.click()

    def closePopupWin(self):
        time.sleep(30)
        self.close_popup()

    # Search flights method
    def SearchSingleRoom(self, location, checkindate, checkoutdate):
        #self.closePopupWin()
        self.clickHotelsTab()
        self.inputHotelLocation(location)
        self.inputCheckinDate(checkindate)
        self.inputCheckoutDate(checkoutdate)
        self.clickTravellerAndHotelField()
        self.inscreaseNumberOfAdults()
        self.clickSearchBtn()

    def SearchMultiRoom(self, location, checkindate, checkoutdate):
        #self.closePopupWin()
        self.clickHotelsTab()
        self.inputHotelLocation(location)
        self.inputCheckinDate(checkindate)
        self.inputCheckoutDate(checkoutdate)
        self.clickTravellerAndHotelField()
        self.inscreaseNumberOfAdults()
        self.inputNewRoom()
        self.addChild()
        self.clickSearchBtn()