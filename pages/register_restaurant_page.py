# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from pages.account_page import AccountPage

class RegisterRestaurantPage(BasePage):
    _title = "Register Restaurant Page"

    _last_name_field = (By.NAME, "name")
    _last_name_value = "AUTOTESTz"+get_random_string(7)
    _address_field = (By.NAME, "address")
    _address_value = get_random_string(7)+" "+get_random_integer(2)
    _zip_code_field = (By.NAME, "zipcode")
    _zip_code_value = get_random_integer(5)
    _city_field = (By.NAME, "city")
    _city_value = get_random_string(7)
    _country_field = (By.NAME, "country")
    _country_value = get_random_string(7)
    _timezone_dropdown = (By.NAME, "timezone")
    _timezone_index = randint(1, 583)
    _random_language = (By.XPATH, "//tr[%s]/td[2]/input" %randint(1,2))
    _email_field = (By.NAME, "email")
    _email_value = get_random_string(7)+"@"+get_random_string(5)+".pl"
    _senders_email_field = (By.NAME, "publicEmail")
    _senders_email_value = get_random_string(7)+"@"+get_random_string(5)+".pl"
    _msgIn_email_field = (By.NAME, "msgInEmail")
    _msgIn_email_value = "msgin@aleno.me"
    _website_field = (By.NAME, "website")
    _website_value = "www."+get_random_string(9)+".waw.pl"
    _facebook_field = (By.NAME, "facebook")
    _facebook_value = get_random_string(8)
    _fan_page_url_field = (By.NAME, "fanPageUrl")
    _fan_page_url_value = "www."+get_random_string(9)+".waw.pl"
    _trip_advisor_field = (By.NAME, "tripadvisor")
    _trip_advisor_value = get_random_string(8)
    _google_field = (By.NAME, "google")
    _google_value = get_random_string(8)
    _yelp_field = (By.NAME, "yelp")
    _yelp_value = get_random_string(7)
    _phone_field = (By.NAME, "phone")
    _phone_value = get_random_integer(9)
    _opening_hours_open_field = (By.XPATH, "//div[22]/div/div")
    _opening_hours_close_field = (By.XPATH, "//div[22]/div/button")
    _opening_hours_field = (By.XPATH, "//div[3]/div[3]")
    _opening_hours_value = get_random_integer(2)+"-"+get_random_integer(2)+": Monday - Friday"
    _image_url_field = (By.NAME, "imageUrl")
    _image_url_value = "http://www.avsforum.com/photopost/data/2277869/9/9f/9f50538d_test.jpeg"
    _random_additional_option = (By.XPATH, "//div[%s]/div/label/input" % randint(25, 30))
    _save_restaurant_button = (By.XPATH, "//form/div[2]/div/button")



    def __init__(self, driver):
        super(RegisterRestaurantPage, self).__init__(driver, self._title)

    def enter_restaurant_data(self, restaurant_name):
        self.clear_field_and_send_keys(restaurant_name, self._last_name_field, "Restaurant last name field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._address_value, self._address_field, "Restaurant address field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._zip_code_value, self._zip_code_field, "Restaurant zip code field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._city_value, self._city_field, "Restaurant city field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._country_value, self._country_field, "Restaurant country field wasn't found on add new restaurant page")
        self.select_index_from_dropdown(self._timezone_index, self._timezone_dropdown, "Restaurant timezone dropdown wasn't found on add new restaurant page")
        # self.condition_click(self._random_language, "Trying to click random language on the register restaurant page was unsuccessful")
        self.clear_field_and_send_keys(self._email_value, self._email_field, "Restaurant email field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._senders_email_value, self._senders_email_field, "Restaurant senders email field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._msgIn_email_value, self._msgIn_email_field, "Restaurant msgIn email field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._website_value, self._website_field, "Restaurant website field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._facebook_value, self._facebook_field, "Restaurant facebook field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._fan_page_url_value, self._fan_page_url_field, "Restaurant fan page url field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._trip_advisor_value, self._trip_advisor_field, "Restaurant trip advisor field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._google_value, self._google_field, "Restaurant google field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._yelp_value, self._yelp_field, "Restaurant yelp field wasn't found on add new restaurant page")
        self.clear_field_and_send_keys(self._phone_value, self._phone_field, "Restaurant phone field wasn't found on add new restaurant page")
        self.click(self._opening_hours_open_field, "Trying to open field \"Opening hours\" to enter text to it was unsuccessful")
        self.clear_field_and_send_keys(self._opening_hours_value, self._opening_hours_field, "Restaurant opening hours field wasn't found on add new restaurant page")
        self.click(self._opening_hours_close_field, "Trying to close field \"Opening hours\" after entering text to it was unsuccessful")
        self.clear_field_and_send_keys(self._image_url_value, self._image_url_field, "Restaurant image url field wasn't found on add new restaurant page")
        self.click(self._random_additional_option, "Trying to click random additional option at the bottom of the register restaurant page was unsuccessful")

    def save_restaurant(self):
        self.click(self._save_restaurant_button, "Save restaurant button wasn't found on the register restaurant page")
        return AccountPage(self.get_driver())






