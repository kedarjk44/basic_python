from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def locate_username_field(self):
        return self.driver.find_element(By.ID, "username")

    def locate_password_field(self):
        return self.driver.find_element(By.ID, "password")

    def locate_login_button(self):
        return self.driver.find_element(By.ID, "login_button")

    def enter_username(self, username):
        username_field = self.locate_username_field()
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.locate_password_field()
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.locate_login_button()
        login_button.click()

import unittest
import csv
from selenium import webdriver
# from page_objects import LoginPage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        with open("login_data.csv") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                username, password = row
                self.login_page.enter_username(username)
                self.login_page.enter_password(password)
                self.login_page.click_login_button()
                # Add assertions here to verify login success or failure
                # For example:
                # self.assertTrue(self.login_page.is_logged_in())


if __name__ == "__main__":
    unittest.main()