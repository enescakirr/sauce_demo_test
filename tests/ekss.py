from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import configparser
import pytest

config = configparser.ConfigParser()
config.read("../../config.ini")


browser = config.get("WebDriverSettings", "browser").lower()
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def goto_souce_demo_page(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def wait_page_name(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login_logo")))

    def driver_quit(self):
        self.driver.quit()


@pytest.fixture(scope="module")
def driver():
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        print(f'Invalid browser type: {browser}')
    driver.set_window_size(1920, 1080)
    yield driver

def test_base_page(driver):
    base_class = BasePage(driver)
    base_class.goto_souce_demo_page()
    base_class.wait_page_name()
    base_class.driver_quit()

