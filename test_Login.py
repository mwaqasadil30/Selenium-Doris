from selenium.webdriver.common.by import By
# from test_Constant_Elements import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_Browsers import *


constant = Constants()

class Login_Locators():

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, constant.WAIT_TIME)
        self.long_wait = WebDriverWait(self.driver, constant.LONG_WAIT)
        self.LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="username"]')
        self.LOGIN_PASSWORD = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/form/div/div[2]/div/div/div/input')
        self.LOGIN_BUTTON = (By.XPATH, '//*[@id="submit"]')

        self.EDIT_SCHEDULE = (By.CSS_SELECTOR, '.schedule-btn-text-container button[aria-label="Edit Schedule"]')
        self.SAVE_BUTTON = (By.CSS_SELECTOR, '.modal-footer .btn-primary')
        self.NOTIFICATION = (By.CSS_SELECTOR, '.Toastify__toast-body .toast-body')


class Login_Implement(Login_Locators):

   def login_functionality(self):

        email_login = self.wait.until(ec.visibility_of_element_located(self.LOGIN_EMAIL))
        email_login.send_keys(constant.EMAIL)
        password_login = self.wait.until(ec.visibility_of_element_located(self.LOGIN_PASSWORD))
        password_login.send_keys(constant.PASSWORD)
        login_button = self.wait.until(ec.visibility_of_element_located(self.LOGIN_BUTTON))
        login_button.click()