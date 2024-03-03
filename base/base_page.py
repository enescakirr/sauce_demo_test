from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import configparser
from selenium import webdriver


config = configparser.ConfigParser()
config.read('../config.ini')

browser = config.get('WebDriverSettings', 'browser').lower()

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def driver(self):
        return self.driver()

    def goto_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def is_element_present(self, locator):
        try:
            self.driver.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except ElementNotVisibleException:
            return False
