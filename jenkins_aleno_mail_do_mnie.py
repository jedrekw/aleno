# coding=utf-8
import unittest
from selenium import webdriver
from htmltestrunner import HTMLTestRunner
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *
from utils.utils import *
from time import sleep
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.remote.webelement import *
from time import gmtime, strftime
import re
from selenium.webdriver.remote.webelement import *
from selenium.webdriver.common.action_chains import *
import datetime as dt
from datetime import datetime
from selenium.common.exceptions import *

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
run_locally = True

# @on_platforms(browsers)


class SmokeTest(unittest.TestCase):
    _internal_non_grouped_domain_text = 1

    def test_SEATIN3_add_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("August test restaurant")
        seatin3_page = account_page.open_seatin3()
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(seatin3_page._seatin3_first_shift_on_list), "First shift on list on seatin3 page didn't show")
            seatin3_page.seatin3_click_first_shift_on_list()
        except WebDriverException as e:
            seatin3_page.seatin3_change_shift()
        seatin3_page.seatin3_add_reservation()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(seatin3_page._seatin3_10_hour_reservation_client_name_field, seatin3_page._seatin3_client_name_value), "The client name (test test) didn't show in the reservation client name field at 10:00 in left panel in seatin3 page, probably the reservation wasn't added")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(seatin3_page._seatin3_reservation_comment_field, seatin3_page._seatin3_reservation_comment_value), "The added reservation comment value didn't show in the comment field for reservation at 10:00 in seatIn3 page")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(seatin3_page._seatin3_10_hour_reservation_start_hour_field, "10:00"), "The reservation start hour (10:00) didn't show in reservation at 10:00 start hour field in seatIn3 page")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(seatin3_page._seatin3_10_hour_reservation_end_hour_field, "10:30"), "The reservation end hour (10:30) didn't show in reservation at 10:00 end hour field in seatIn3 page")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(seatin3_page._seatin3_10_hour_reservation_person_field, "5"), "The reservation number of people (5) didn't show in reservation at 10:00 number of people field in seatIn3 page")

        seatin3_page.seatin3_remove_added_reservation()

        WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(seatin3_page._seatin3_10_hour_reservation_client_name_field, seatin3_page._seatin3_client_name_value), "The reservation client name (test test) was shown in the reservation client name field at 10:00 in left panel in seatIn3, although it shouldn't, because the reservation was supposed to be removed")

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.startup.homepage", "about:blank")
            fp.set_preference("startup.homepage_welcome_url", "about:blank")
            fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            fp.set_preference(" xpinstall.signatures.required", "false")
            fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            binary = FirefoxBinary('/__stare/firefox45/firefox')
            self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
            self.driver.set_window_size(1024,768)
            self.driver.implicitly_wait(self.timeout)
            self.errors_and_failures = self.tally()
        else:
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
            )

            self.driver.implicitly_wait(self.timeout)

    def tearDown(self):
        if run_locally:
                if self.tally() > self.errors_and_failures:
                    if not os.path.exists(SCREEN_DUMP_LOCATION):
                        os.makedirs(SCREEN_DUMP_LOCATION)
                    for ix, handle in enumerate(self.driver.window_handles):
                        self._windowid = ix
                        self.driver.switch_to.window(handle)
                        self.take_screenshot()
                        self.dump_html()
                self.driver.quit()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename = "{classname}.{method}-window{windowid}-{timestamp}".format(
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )
        return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )

    def _get_filename_for_plot(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename_plot = "{classname}.plot-{timestamp}".format(
            classname=self.__class__.__name__,
            timestamp=timestamp
        )
        return "{folder}/{classname}.plot-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            timestamp=timestamp
            )

    def _save_plot(self):
        import matplotlib.pyplot as plt
        filename = self._get_filename_for_plot() + ".png"
        err = len(self._resultForDoCleanups.errors)
        fail = len(self._resultForDoCleanups.failures)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Failures', 'Passes'
        sizes = [err, fail, 18-fail-err]
        colors = ['red', 'gold', 'green']
        explode = (0.1, 0.1, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        print "\n WYKRES:\n", filename
        plt.savefig(filename)
        text_file = open("AlenoRaportScreeny.txt", "a")
        text_file.write("<br><br>Wykres statystyczny: <a href=""http://ci.testuj.pl/job/Aleno/ws/screendumps/"+self._saved_filename_plot+".png>Wykres</a>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("AlenoRaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Aleno/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("AlenoRaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Aleno/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["jedrzej.wojcieszczyk@testuj.pl"])
        message.Subject = "Raport Jenkins Aleno Testy Automatyczne"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Aleno.pl<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny: <a href="http://ci.testuj.pl/job/Aleno/ws/AlenoReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
        sender.send(message)

    def not_contains(self, needle, haystack, msg=''):
        try:
            assert not needle in haystack
        except AssertionError:
            raise AssertionError('%s is found in %s. %s' % (needle, haystack, msg))

    def is_element_present(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

open("AlenoRaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("AlenoReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Aleno', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
# if __name__ == '__main__':
#      unittest.main()

     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))