from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import os


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def read_config(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_directory, '../requirements/config.ini')
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config.get('WebDriverSettings', 'browser').lower()

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
