from base.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class LoginPage(BasePage):

    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_element_load(self):
        self.wait.until(EC.visibility_of_element_located(self.user_name))
        self.wait.until(EC.visibility_of_element_located(self.password))
        self.wait.until(EC.visibility_of_element_located(self.login_button))

    def input_username(self, username):
        self.driver.find_element(*self.user_name).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
        return HomePage(self.driver)
