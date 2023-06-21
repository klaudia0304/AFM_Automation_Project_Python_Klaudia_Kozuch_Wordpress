from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    MY_SITE_BTN=(By.XPATH,'//span[text()="My Site"]')
    WRITE_BTN=(By.XPATH,'//div//a[@title="Create a New Post"]')
    CREATE_SITE_BTN=(By.XPATH, '//a[text()="Create Site"]')
    DOMAIN_INPUT=(By.XPATH,'//form/input[@type="search"]')
    FIELD_WITH_DOMAIN=(By.XPATH,'//div//span[text()="Free"]')
    SELECT_BTN=(By.XPATH,"(//div//div[contains(., '.wordpress.com')]/following-sibling::div//button[text()='Select'])[1]")
    START_FREE_BTN=(By.XPATH,'(//div//div//button[text()="Start with Free"])[1]')
    WRITE_AND_PUBLISH_BTN=(By.XPATH,'(//div[@class="components-base-control components-checkbox-control css-qy3gpb ej5x27r4"])[1]')
    CONTINUE_BTN=(By.XPATH,'//div//button[text()="Continue"]')
    TITLE_INPUT=(By.XPATH,'//input[@value="Site Title"]')
    CONTINUE_BTN2=(By.XPATH,'//button[text()="Continue"]')
    SKIP_BTN=(By.XPATH,'//button[text()="Skip to dashboard"]')


class MainPage(BasePage):
    def locate_mysite_btn(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.MY_SITE_BTN)
        )
        return el

    def click_write_btn(self):
        el = self.driver.find_element(*Locators.WRITE_BTN)
        el.click()

    def click_create_site(self):
        # Wait for the element to be present in the DOM and clickable
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CREATE_SITE_BTN)
        )
        el.click()

    def type_domain_name(self,domain_name):
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.DOMAIN_INPUT)
        )
        el.send_keys(domain_name)

    def select_free_domain(self):
        el = self.driver.find_element(*Locators.SELECT_BTN)
        el.click()

    def start_with_free(self):
        el = self.driver.find_element(*Locators.START_FREE_BTN)
        el.click()

    def click_checkbox(self):
        el = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Locators.WRITE_AND_PUBLISH_BTN)
        )
        el.click()

    def click_continue(self):
        el = self.driver.find_element(*Locators.CONTINUE_BTN)
        el.click()

    def add_blog_name(self,title):
        el = self.driver.find_element(*Locators.TITLE_INPUT)
        el.clear()
        el.click()
        el.send_keys(title)

    def click_continue2(self):
        el = self.driver.find_element(*Locators.CONTINUE_BTN2)
        el.click()

    def skip_to_dashboard(self):
        el = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Locators.SKIP_BTN)
        )
        el.click()
