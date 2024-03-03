import pytest
import configparser

from selenium import webdriver
from pages.login_page import LoginPage
from base.base_page import BasePage

# config = configparser.ConfigParser()
# config.read('config.ini')

# browser = config.get('WebDriverSettings', 'browser').lower()

browser = 'chrome'


class TestLoginPage:

    @pytest.fixture(scope="module")
    def driver(self):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'safari':
            driver = webdriver.Safari()
        else:
            print(f'Browser {browser} not supported this software!')
        driver.maximize_window()
        yield driver

    def test_login_with_correct_username_and_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("standard_user")
        login_page.input_password("secret_sauce")
        home_page = login_page.click_login_button()
        home_page.wait_element_load()
        assert home_page.logo_element().text == "Swag Labs", "Login failed with correct username and password!"
