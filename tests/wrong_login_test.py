import unittest
from selenium import webdriver
from pages.login_page import LoginPage
import time


class WrongCredentialsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_wrong_credentials(self):
        login_page = LoginPage(self.driver)

        # 1. go to page https://www.saucedemo.com/
        login_page.visit()
        login_page.log_in_website_check()

        # 2. type incorrect credentials
        login_page.log_in('any_user', 'secret_pass')

        # 3. check if notification: 'Username and password do not match any user in this service' is displayed# noqa
        messages_text = login_page.wrong_credentials_alert()
        self.assertEqual('Epic sadface: Username and password do not match any user in this service', messages_text,# noqa
                         f'Expected login button text differ from actual: {messages_text}')# noqa

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
