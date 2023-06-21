from pages.blog_page import BlogPage
from pages.main_page import MainPage
from tests.base_test import BaseTest
from time import sleep
from faker import Faker
from tests.login_test import USERNAME, PASSWORD

fake=Faker()


class BlogTest(BaseTest):
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
        main_page_object = MainPage(self.driver)
        main_page_object.skip_to_dashboard()
        sleep(2)

    #TC5
    def testAddingElements(self):
        #1 Click button skip to dashboard to go to main page
        blog_page_object = BlogPage(self.driver)
        sleep(2)
        #2 Click Pages button
        blog_page_object.click_on_pages()
        sleep(2)
        #3 Click Add new page button
        blog_page_object.click_create_page()
        sleep(5)
        #4 Click Create Blank button
        blog_page_object.create_blank_page()
        sleep(2)
        #5 Add title in input field
        fake_title = fake.catch_phrase()
        blog_page_object.add_title(fake_title)
        #6 Verify if added title is present on the page
        self.assertEqual(fake_title, blog_page_object.get_title())
        sleep(2)
        #7 Click Add new element button
        blog_page_object.add_element()
        sleep(2)
        #8 Click Media button
        blog_page_object.add_media()
        sleep(2)
        #9 Click Openverse button
        blog_page_object.open_openverse()
        sleep(2)
        #10 Add text in search input
        blog_page_object.openverse_search_image(fake.word())
        sleep(2)
        #11 Click first image on the images list
        blog_page_object.add_image()
        sleep(2)
        #12 Verify if added image is present on the page
        blog_page_object.verify_if_image_added()
        result = blog_page_object.verify_if_image_added()
        self.assertEqual(1, result)
        sleep(2)
        #13 Click Publish button
        blog_page_object.publish_page()
        sleep(2)
        #14 Click second Publish button
        blog_page_object.publish_page2()
        sleep(2)
        #15 Click second Publish button
        page_url = blog_page_object.get_page_url()
        self.driver.get(page_url)
        sleep(15)
