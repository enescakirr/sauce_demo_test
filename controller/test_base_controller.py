from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import configparser
import pytest

config = configparser.ConfigParser()
config.read('../config.ini')

browser = config.get('WebDriverSettings', 'browser').lower()
window_width = int(config.get('WebDriverSettings', 'window_width'))
window_height = int(config.get('WebDriverSettings', 'window_height'))


class TestClass:

    def __init__(self, build_web_driver):
        self.driver = build_web_driver

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def wait_page_name(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))

    def refresh_page(self):
        self.driver.refresh()

    def driver_quit(self):
        self.driver.quit()


@pytest.fixture(scope="module")
def build_web_driver():
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'safari':
        driver = webdriver.Safari()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'{browser}, browser not supported for this software!')
    driver.set_window_size(window_width, window_height)
    yield driver

def test_refresh_page(build_web_driver):
    test_class = TestClass(build_web_driver)
    test_class.open_page()
    test_class.refresh_page()
    test_class.driver_quit()
