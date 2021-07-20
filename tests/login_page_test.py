import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.hamburger_menu_page import HamburgerMenuPage
import time


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_login_check(self):
        login_page = LoginPage(self.driver)
        burger_menu_page = HamburgerMenuPage(self.driver)

        # 1. go to page https://www.saucedemo.com/
        login_page.visit()
        login_page.log_in_website_check()

        # 2. type credentials
        shop_page = login_page.log_in('standard_user', 'secret_sauce')

        # 3. check page title
        messages_text = shop_page.get_messages_text()
        self.assertEqual('PRODUCTS', messages_text,
                         f'Expected login button text differ from actual: {messages_text}')# noqa

        # 4. log out from shop and check if you are logged out
        burger_menu_page.log_out()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
