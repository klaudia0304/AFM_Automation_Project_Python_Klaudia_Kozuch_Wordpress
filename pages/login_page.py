from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    USERNAME_INPUT = (By.XPATH, '//div//input[@id="usernameOrEmail"]')
    USERNAME_CONTINUE_BTN = (By.XPATH, '//div//button[text()="Continue"]')
    PASSWORD_INPUT = (By.XPATH, '//div//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//div//button[text()="Log In"]')
    ERROR_MSG_USER = (By.XPATH, '//div//span[text()="User does not exist."]')
    ERROR_MSG_PASS = (By.XPATH, '//div[@class="form-input-validation is-error"]//span')


class LoginPage(BasePage):
    def enter_username(self, username):
        el = self.driver.find_element(*Locators.USERNAME_INPUT)
        el.click()
        el.send_keys(username)

    def click_continue(self):
        el = self.driver.find_element(*Locators.USERNAME_CONTINUE_BTN)
        el.click()

    def enter_password(self, password):
        el = self.driver.find_element(*Locators.PASSWORD_INPUT)
        el.click()
        el.send_keys(password)

    def click_log_in(self):
        el = self.driver.find_element(*Locators.LOGIN_BTN)
        el.click()

    def get_error_user(self):
        el = self.driver.find_element(*Locators.ERROR_MSG_USER).text
        return el

    def get_error_pass(self):
        el = self.driver.find_element(*Locators.ERROR_MSG_PASS).text
        return el
