from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    PAGES_BTN=(By.XPATH, '//a//span[text()="Pages"]')
    ADD_PAGE_BTN=(By.XPATH, '//a[text()="Add new page"]')
    ADD_BLANK_PAGE_BTN=(By.XPATH, '//div//button[text()="Blank page"]')
    ADD_ELEMENT_BTN=(By.XPATH, '//button[@aria-label="Toggle block inserter"]')
    ADD_MEDIA_BTN=(By.XPATH, '//button[text()="Media"]')
    OPEN_OPENVERSE_BTN=(By.XPATH, '//button[@aria-label="Openverse"]')
    OPENVERSE_SEARCH=(By.XPATH,'//div//input[@placeholder="Search Openverse"]')
    OPENVERSE_IMAGE=(By.XPATH,'(//div[@class="block-editor-inserter__media-list__list-item"])[1]')
    ADDED_TITLE=(By.XPATH,'//h1[@aria-label="Add title"]')
    IFRAME_ELEMENT_IS_LOADED=(By.XPATH, '//iframe[@class="is-loaded"]')
    IFRAME_ELEMENT_CANVAS=(By.XPATH, '//iframe[@name="editor-canvas"]')
    ADDED_IMAGE=(By.XPATH, '//img[starts-with(@alt,"This image has an empty alt attribute")]')
    PUBLISH_BTN=(By.XPATH, '//button[text()="Publish"]')
    PUBLISH_BTN2=(By.XPATH, '//button[@class="components-button editor-post-publish-button editor-post-publish-button__button is-primary"]')
    PAGE_URL_FIELD=(By.XPATH, '//input[@class="components-text-control__input"]')


class BlogPage(BasePage):
    def switch_to_iframe(self, iframe_locator):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(iframe_locator)
        )

    def switch_to_iframe_2_elements(self, iframe_locator1, iframe_locator2):
        self.switch_to_iframe(iframe_locator1)
        self.switch_to_iframe(iframe_locator2)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def click_on_pages(self):
        el = self.driver.find_element(*Locators.PAGES_BTN)
        el.click()

    def click_create_page(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ADD_PAGE_BTN)
        )
        el.click()

    def create_blank_page(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.ADD_BLANK_PAGE_BTN)
        )
        el.click()

        self.switch_to_default_content()

    def add_title(self, title):
        self.switch_to_iframe_2_elements(Locators.IFRAME_ELEMENT_IS_LOADED, Locators.IFRAME_ELEMENT_CANVAS)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.ADDED_TITLE)
        )
        el.click()
        el.send_keys(title)

        self.switch_to_default_content()

    def get_title(self):
        self.switch_to_iframe_2_elements(Locators.IFRAME_ELEMENT_IS_LOADED, Locators.IFRAME_ELEMENT_CANVAS)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.ADDED_TITLE)
        ).text

        self.switch_to_default_content()

        return el

    def add_element(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.ADD_ELEMENT_BTN)
        )
        el.click()

        self.switch_to_default_content()

    def add_media(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.ADD_MEDIA_BTN)
        )
        el.click()

        self.switch_to_default_content()

    def open_openverse(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.OPEN_OPENVERSE_BTN)
        )
        el.click()

        self.switch_to_default_content()

    def openverse_search_image(self,image_topic):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.OPENVERSE_SEARCH)
        )
        el.click()
        el.send_keys(image_topic)

        self.switch_to_default_content()

    def add_image(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.OPENVERSE_IMAGE)
        )
        el.click()

        self.switch_to_default_content()

    def verify_if_image_added(self):
        self.switch_to_iframe_2_elements(Locators.IFRAME_ELEMENT_IS_LOADED, Locators.IFRAME_ELEMENT_CANVAS)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.ADDED_IMAGE)
        )
        if el:
            result = 1
        else:
            result = 0

        self.switch_to_default_content()
        return result

    def publish_page(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.PUBLISH_BTN)
        )
        el.click()

        self.switch_to_default_content()

    def publish_page2(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.PUBLISH_BTN2)
        )
        el.click()

        self.switch_to_default_content()

    def get_page_url(self):
        self.switch_to_iframe(Locators.IFRAME_ELEMENT_IS_LOADED)

        el = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.PAGE_URL_FIELD)
        )
        url = el.get_attribute("value")
        print("Page URL:", url)

        self.switch_to_default_content()
        return url
