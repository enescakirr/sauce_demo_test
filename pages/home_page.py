from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class HomePage(BasePage):

    logo = (By.CLASS_NAME, 'app_logo')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_element_load(self):
        self.wait.until(EC.visibility_of_element_located(self.logo))

    def logo_element(self):
        return self.driver.find_element(*self.logo)
