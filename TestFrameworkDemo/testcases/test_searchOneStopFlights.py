import time

import pytest
import softest
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.hotel_search_page import HotelSearchPage
from pages.search_flights_results_page import SearchFlightsResults
from pages.search_hotels_results_page import SearchHotelsResults
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt()
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    '''@pytest.fixture(autouse=True)
    #@pytest.mark.multiple
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.check = Utils()'''

    @data(("New Delhi", "JFK", "14/09/2023", "1 Stop"), ("Goa", "Melbourne", "15/09/2023", "2 Stops"))
    @unpack
    # @file_data("../Testdata/testData.json")
    def test_search_flights_1_stop(self, goingfrom, goingto, arivaldate, stops):
        lp = LaunchPage(self.driver)
        # lp.departfrom("New Delhi")
        '''lp.inputDepartFromLocation("New Delhi")
        lp.inputGoingToLocation("New York")
        lp.inputGoingToDate("01/09/2023")
        lp.clickSearchBtn()'''
        sf = lp.SearchFlights(goingfrom, goingto, arivaldate)
        # lp.page_scroll()
        # sf = SearchFlightsResults(self.driver)
        sf.page_scroll()
        sf.filter_flights(stops)
        # allStops = sf.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(), '1 Stop') or contains(text(), '2 Stops') or contains(text(), 'Non Stop')]")
        allStops = sf.getSearchFlightsResults()
        self.log.debug("Number of stops {0}: ".format(len(allStops)))
        check = Utils()
        check.assertListItemText(allStops, stops)

    #@data(("New Delhi", "John F Kennedy", "19/09/2023", "17/10/2023", "1 Stop"),
          #("Goa", "Melbourne", "19/09/2023", "16/10/2023", "2 Stops"))
    #@unpack
    @file_data("../Testdata/testData.json")
    def test_search_round_trip(self, goingfrom, goingto, arivaldate, returndate, stops):
        lp = LaunchPage(self.driver)
        # lp.departfrom("New Delhi")
        '''lp.inputDepartFromLocation("New Delhi")
        lp.inputGoingToLocation("New York")
        lp.inputGoingToDate("01/09/2023")
        lp.clickSearchBtn()'''
        sf = lp.SearchRoundTripFlights(goingfrom, goingto, arivaldate, returndate)
        # lp.page_scroll()
        # sf = SearchFlightsResults(self.driver)
        sf.page_scroll()
        sf.filter_flights(stops)
        # allStops = sf.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(), '1 Stop') or contains(text(), '2 Stops') or contains(text(), 'Non Stop')]")
        allStops = sf.getSearchFlightsResults()
        self.log.debug("Number of stops {0}: ".format(len(allStops)))
        check = Utils()
        check.assertListItemText(allStops, stops)

    '''def test_search_flights_2_stops(self):
        lp = LaunchPage(self.driver)
        # lp.departfrom("New Delhi")
        #lp.inputDepartFromLocation("New Delhi")
        #lp.inputGoingToLocation("New York")
        #lp.inputGoingToDate("31/08/2023")
        #lp.clickSearchBtn()
        sf = lp.SearchFlights("New Delhi", "New York", "08/09/2023")
        # lp.page_scroll()
        # sf = SearchFlightsResults(self.driver)
        sf.page_scroll()
        sf.filter_flights("2 Stops")
        # allStops = sf.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(), '1 Stop') or contains(text(), '2 Stops') or contains(text(), 'Non Stop')]")
        allStops = sf.getSearchFlightsResults()
        self.log.debug("Number of stops {0}: ".format(len(allStops)))
        check = Utils()
        check.assertListItemText(allStops, "2 Stops")'''

    @data(("New Delhi", "27/11/2023", "17/12/2023", "3+"))
    @unpack
    # @file_data("../Testdata/testData.json")
    def test_hotel_single_room(self, location, checkindate, checkoutdate, ratings):
        shp = HotelSearchPage(self.driver)
        shp.SearchSingleRoom(location, checkindate, checkoutdate)
        hrp = SearchHotelsResults(self.driver)
        hrp.page_scroll()
        hrp.filter_hotels(ratings)
        hotel_results = hrp.getAllRatingsIcon()
        self.log.debug("Number of hotels {0}: ".format(len(hotel_results)))
        check = Utils()
        check.assertRatingsText(hotel_results, ratings)

    @data(("New Delhi", "27/11/2023", "17/12/2023", "3+"))
    @unpack
    # @file_data("../Testdata/testData.json")
    def test_hotel_multiple_room(self, location, checkindate, checkoutdate, ratings):
        shp = HotelSearchPage(self.driver)
        shp.SearchMultiRoom(location, checkindate, checkoutdate)
        hrp = SearchHotelsResults(self.driver)
        hrp.page_scroll()
        hrp.filter_hotels(ratings)
        hotel_results = hrp.getAllRatingsIcon()
        self.log.debug("Number of hotels {0}: ".format(len(hotel_results)))
        check = Utils()
        check.assertRatingsText(hotel_results, ratings)
