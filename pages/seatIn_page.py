# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SeatInPage(BasePage):
    _title = "SeatIn Page"

    _add_reservation_plus_button = (By.XPATH, '//button[@title="Neue Reservation"]')
    _add_reservation_plus_button2 = (By.XPATH, "//div[2]/div/button")
    _add_reservation_hour_button = (By.XPATH, "//div[2]/div/div/div[3]/div")
    _add_reservation_details_button = (By.XPATH, "//button[@title='Details']")
    _add_reservation_first_accordeon = (By.XPATH, "//form/div/div/div/a")
    _add_reservation_guests_field = (By.NAME, "peopleCount")
    _add_reservation_guests_value = randint(2, 8)
    _add_reservation_start_time_field = (By.NAME, "selectedTime")
    # _add_reservation_start_time_value = "15:00"
    _add_reservation_second_accordeon = (By.XPATH, "//form/div/div[2]/div/a")
    _add_reservation_language_dropdown = (By.NAME, "lang")
    _add_reservation_phone_field = (By.NAME, "phoneNumber")
    _add_reservation_phone_value = get_random_integer(9)
    _add_reservation_first_name_field = (By.NAME, "firstName")
    _add_reservation_first_name_value = get_random_string(8)
    _add_reservation_surname_field = (By.NAME, "lastName")
    _add_reservation_email_field = (By.NAME, "email")
    _add_reservation_email_value = get_random_string(7)+"@"+get_random_string(5)+".pl"
    _add_reservation_status_dropdown = (By.NAME, "state")
    _add_reservation_email_benachrichtigung_checkbox = (By.NAME, "resendStateTemplate")
    _add_reservation_send_sms_e_mail_reminder = (By.NAME, "sendReminderEmailTemplate")
    _add_reservation_edited_by_header = (By.XPATH, "//div[12]/div[2]/label")
    # _add_reservation_fourth_accordeon = (By.LINK_TEXT, "Comments")
    # _add_reservation_guests_comment_open_field = (By.NAME, "comment")
    # _add_reservation_guests_comment_close_field = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/div[1]/div/div/button")
    # _add_reservation_guests_comment_field = (By.XPATH, "//div[3]/div[3]")
    # _add_reservation_guests_comment_value = get_random_string(6)+" "+get_random_string(7)+" "+get_random_string(8)
    # _add_reservation_internal_comment_open_field = (By.NAME, "internalComment")
    # _add_reservation_internal_comment_close_field = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/div[2]/div/div/button")
    # _add_reservation_internal_comment_field = (By.XPATH, "//div[2]/div/div/div[2]/div[3]/div[3]/p")
    # _add_reservation_internal_comment_value = get_random_string(8)+" "+get_random_string(7)+" "+get_random_string(6)
    _save_reservation_button = (By.CSS_SELECTOR, "html.bg-aleno.scroll-y body div.wrap div.main-header-wrapper div.main-top-subnav-wrapper div.main-top-subnavigation div.container div.col-sm-6.text-right.toolbar-lh button.js-submit-form.btn.btn-default.btn-success")
    _expand_seatIn_reservation_details_button = (By.XPATH, "//div[2]/div/div/div[3]/button")
    _added_reservation = (By.XPATH, "//*[text()='" + _add_reservation_first_name_value + "']")
    _remove_added_reservation_button = (By.LINK_TEXT, "Storniert")
    _shift_name_field = (By.CSS_SELECTOR, "span.shiftName")
    _seatIn_room_separator_field = (By.CSS_SELECTOR, "div.ce-room-separator")

    def __init__(self, driver):
        super(SeatInPage, self).__init__(driver, self._title)
        self._add_reservation_surname_value = get_random_string(9)

    def click_add_reservation_plus_button(self):
        self.click(self._add_reservation_plus_button)

    def click_hour(self):
        self.click(self._add_reservation_hour_button)

    def click_reservation_details_button(self):
        self.click(self._add_reservation_details_button)

    def reservation_open_first_accordeon(self):
        self.click(self._add_reservation_first_accordeon)

    def enter_reservation_details(self, start_time):
        self.clear_field_and_send_keys(self._add_reservation_guests_value, self._add_reservation_guests_field)
        self.clear_field_and_send_keys(start_time, self._add_reservation_start_time_field)
        self.click(self._add_reservation_second_accordeon)
        # self.select_index_from_dropdown(0, self._add_reservation_language_dropdown)
        self.clear_field_and_send_keys(self._add_reservation_phone_value, self._add_reservation_phone_field)
        self.clear_field_and_send_keys(self._add_reservation_first_name_value, self._add_reservation_first_name_field)
        self.clear_field_and_send_keys(self._add_reservation_surname_value, self._add_reservation_surname_field)
        self.clear_field_and_send_keys(self._add_reservation_email_value, self._add_reservation_email_field)
        WebDriverWait(self.get_driver(), 60).until(EC.text_to_be_present_in_element(self._add_reservation_edited_by_header, "Bearbeitet von"))
        # self.click(self._add_reservation_fourth_accordeon)
        # sleep(2)
        # self.click(self._add_reservation_guests_comment_open_field)
        # self.clear_field_and_send_keys(self._add_reservation_guests_comment_value, self._add_reservation_guests_comment_field)
        # self.click(self._add_reservation_guests_comment_close_field)
        # self.click(self._add_reservation_internal_comment_open_field)
        # self.clear_field_and_send_keys(self._add_reservation_internal_comment_value, self._add_reservation_internal_comment_field)
        # self.click(self._add_reservation_internal_comment_close_field)

    def reservation_set_provisional(self):
        self.select_index_from_dropdown(0, self._add_reservation_status_dropdown)

    def reservation_set_email_sms_notifications(self):
        self.click(self._add_reservation_email_benachrichtigung_checkbox)
        self.click(self._add_reservation_send_sms_e_mail_reminder)

    def save_reservation(self):
        self.click(self._save_reservation_button)

    def expand_seatIn_reservation_details(self):
        self.click(self._expand_seatIn_reservation_details_button)

    def click_added_reservation(self):
        self.click(self._added_reservation)

    def remove_added_reservation(self):
        self.click(self._remove_added_reservation_button)
        self.accept_alert()
        sleep(2)







