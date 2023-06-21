from pages.main_page import MainPage
from tests.base_test import BaseTest
from time import sleep
from faker import Faker
from tests.login_test import USERNAME, PASSWORD

fake=Faker()


class MainTest(BaseTest):
    def setUp(self):
        super().setUp()
        login_page_object = self.home_page_object.click_log_in()
        sleep(1)
        login_page_object.enter_username(USERNAME)
        sleep(1)
        login_page_object.click_continue()
        sleep(1)
        login_page_object.enter_password(PASSWORD)
        sleep(1)
        login_page_object.click_log_in()
        sleep(1)

    #TC4
    def test_create_site(self):
        #1 Click button skip to dashboard to go to main page
        main_page_object = MainPage(self.driver)
        sleep(2)
        #2 Click Write button
        main_page_object.click_write_btn()
        sleep(2)
        #3 Click Create Site button
        main_page_object.click_create_site()
        sleep(2)
        #4 Add domain name in input field
        main_page_object.type_domain_name("koautoqa"+fake.domain_word()+".wordpress.com")
        sleep(2)
        #5 Click Select by the free domain option
        main_page_object.select_free_domain()
        sleep(2)
        #6 Click Start with Free button
        main_page_object.start_with_free()
        sleep(2)
        #7 Click Write&Publish checkbox
        main_page_object.click_checkbox()
        sleep(2)
        #8 Click Continue button
        main_page_object.click_continue()
        sleep(2)
        #9 Add blog title in input field
        main_page_object.add_blog_name(fake.catch_phrase())
        sleep(2)
        #10 Click Continue button
        main_page_object.click_continue2()
        sleep(2)
        #11 Click button skip to dashboard to go to main page
        main_page_object.skip_to_dashboard()
        sleep(2)
        #12 Click button skip to dashboard to go to main page
        main_page_object.skip_to_dashboard()
        sleep(2)