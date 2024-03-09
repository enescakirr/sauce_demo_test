import pytest

from selenium import webdriver
from pages.login_page import LoginPage
from base.base_page import BasePage


class TestLoginPage:

    @pytest.fixture(scope="module")
    def driver(self):
        login_page = LoginPage(BasePage)
        if login_page.read_config() == 'chrome':
            driver = webdriver.Chrome()
        elif login_page.read_config() == 'firefox':
            driver = webdriver.Firefox()
        elif login_page.read_config() == 'safari':
            driver = webdriver.Safari()
        else:
            print(f'Browser {login_page.read_config()} not supported this software!')
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

    def test_login_with_correct_username_and_wrong_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("standard_user")
        login_page.input_password("wrong_password")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Username and password do not match any user in this service", "Correct username and wrong password case failed!"

    def test_login_with_correct_username_and_empty_password(self,driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("standard_user")
        login_page.input_password("")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Password is required", "Correct username and empty password case failed!"

    def test_login_wrong_username_and_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("wrong_username")
        login_page.input_password("wrong_password")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Username and password do not match any user in this service", "Wrong username and password case failed!"

    def test_login_wrong_username_and_correct_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("wrong_username")
        login_page.input_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Username and password do not match any user in this service", "Wrong username and correct password case failed!"

    def test_login_wrong_username_and_empty_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("wrong_username")
        login_page.input_password("")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Password is required", "Wrong username and empty password case failed!"

    def test_login_empty_username_and_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("")
        login_page.input_password("")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Username and password required", "Empty username and password case failed!"

    def test_login_empty_username_and_correct_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("")
        login_page.input_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Username is required", "Empty username and correct password case failed!"

    def test_login_empty_username_and_wrong_password(self, driver):
        base_page = BasePage(driver)
        base_page.goto_page()
        login_page = LoginPage(driver)
        login_page.wait_element_load()
        login_page.input_username("")
        login_page.input_password("wrong_password")
        login_page.click_login_button()
        assert login_page.error_message() == "Epic sadface: Username is required", "Empty username and wrong password case failed!"
