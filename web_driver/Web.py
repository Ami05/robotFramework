from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webDriverManager import webDriverManager
import time

class Web(object):
    _driver = None

    def __init__(self, browser):
        self._driver = webDriverManager.get_web_driver(browser)
        #self._driver.maximize_window()
        self._wait = WebDriverWait(self._driver, 10)

    def get_web_element_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_web_elements_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def execute_script(self, script):
        return self._driver.execute_script(script)

    def selectDate(self):
        self._driver.find_element_by_css_selector("input#datepicker2").click()
        time.sleep(4)
        self._driver.find_element_by_css_selector("div#ui-datepicker-div tbody td.ui-datepicker-week-end:not(.ui-state-disabled)").click()   


    def open(self, path):
        self._driver.get(path)

    def close_all(self):
        self._driver.quit()
        print("")