from pages.main_page import MainPage
from tests.base_test import BaseTest
from time import sleep
from faker import Faker

fake=Faker()

#Test data
USERNAME = "koautoqa@gmail.com"
PASSWORD = "@uToT3STpYTh"
ERRORMESSAGE_EXPECTED="User does not exist. Would you like to create a new account?"
ERRORMESSAGE_EXPECTED_PASS="Oops, that's not the right password. Please try again!"


class LoginTest(BaseTest):
    #TC1
    def test_log_in_with_valid_credentials(self):
        #1 Click Login button
        login_page_object = self.home_page_object.click_log_in()
        sleep(2)
        #2 Add Username to input field
        login_page_object.enter_username(USERNAME)
        #3 Click continue
        login_page_object.click_continue()
        sleep(2)
        #4 Add Password to input field
        login_page_object.enter_password(PASSWORD)
        #5 Click login
        login_page_object.click_log_in()
        sleep(4)
        #6 Verify if you are logged in - check if My Site button is present
        self.main_page_object = MainPage(self.driver)
        self.assertEqual("My Site", self.main_page_object.locate_mysite_btn().text)
        sleep(2)

    #TC2
    def test_unregistered_user_error(self): #metoda testowa
        #1 Click login
        login_page_object=self.home_page_object.click_log_in()
        sleep(2)
        #2 Add incorrect Username to input field
        login_page_object.enter_username(fake.email())
        sleep(2)
        #3 Click continue
        login_page_object.click_continue()
        sleep(2)
        #4 Verify error mesage
        self.assertEqual(ERRORMESSAGE_EXPECTED, login_page_object.get_error_user())
        sleep(2)

    #TC3
    def test_incorrect_password(self): #metoda testowa
        #1 Click login
        login_page_object=self.home_page_object.click_log_in()
        sleep(1)
        #2 Add Username to input field
        login_page_object.enter_username(USERNAME)
        sleep(1)
        #3 Click continue
        login_page_object.click_continue()
        sleep(2)
        #4 Add incorrect Password to input field
        login_page_object.enter_password(fake.password())
        sleep(2)
        #5 Click login
        login_page_object.click_log_in()
        sleep(2)
        #6 Verify error mesage
        self.assertEqual(ERRORMESSAGE_EXPECTED_PASS, login_page_object.get_error_pass())
        sleep(2)



