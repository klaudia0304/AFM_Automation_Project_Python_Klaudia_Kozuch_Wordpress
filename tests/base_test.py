from pages.home_page import HomePage
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase): #dziedziczymy z unittesta test case
    #klasa bazowa każdego testu
    def setUp(self):
        #Open browser
        self.driver = webdriver.Chrome() #tu mam stworzony driver który musze użyć jako argument w login_test.py
        #maksymalizuj okno
        self.driver.maximize_window()
        #wejdz na strone główną
        self.driver.get("https://wordpress.com/")
        # Utwórz instancję HomePage
        self.home_page_object = HomePage(self.driver)
        #dodaj wait na element 5 sek
        self.driver.implicitly_wait(5)


    def tearDown(self):
        #wyłącz przeglądarkę
        self.driver.quit()
    pass