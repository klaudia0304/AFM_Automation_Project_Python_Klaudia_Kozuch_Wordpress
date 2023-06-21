from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BTN=(By.XPATH,'//li[@class="x-nav-item x-nav-item--wide"]//a[@title="Log In"]')


class HomePage(BasePage):
    def click_log_in(self):
        el=self.driver.find_element(*Locators.LOGIN_BTN)
        el.click()
        return LoginPage(self.driver)
