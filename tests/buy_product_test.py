import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.hamburger_menu_page import HamburgerMenuPage
from pages.sauce_shop_main_page import SaucePage
from pages.cart_page import CartPage
from pages.checkout_information_page import CartInfo
from pages.checkout_overview_page import CartOverview
from pages.checkout_complete_page import CartComplete
import time


class BuyProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_buy_product(self):
        login_page = LoginPage(self.driver)
        burger_menu_page = HamburgerMenuPage(self.driver)
        add_product = SaucePage(self.driver)
        check_product_cart = CartPage(self.driver)
        check_info = CartInfo(self.driver)
        check_overview = CartOverview(self.driver)
        check_complete = CartComplete(self.driver)

        # 1. go to page https://www.saucedemo.com/
        login_page.visit()
        login_page.log_in_website_check()

        # 2. type credentials
        login_page.log_in('standard_user', 'secret_sauce')

        # 3. reset app state
        burger_menu_page.reset_app_state()

        # 4. add product into cart
        add_product.add_tshirt_to_cart()

        # 5. check if product is added into cart
        product_text = check_product_cart.check_product_in_cart()
        self.assertEqual('Sauce Labs Bolt T-Shirt', product_text,
                         f'Expected login button text differ from actual: {product_text}')# noqa
        time.sleep(3)

        # 6. make checkout of your shopping
        check_product_cart.click_checkout()
        check_title_text = check_info.check_title_text()
        self.assertEqual('CHECKOUT: YOUR INFORMATION', check_title_text,
                         f'Expected login button text differ from actual: {check_title_text}')# noqa

        # 7. fill personal data
        check_info.fill_personal_data('John', 'Test', '22-222')

        # 8. make shopping overview and click 'FINISH' button
        check_overview_text = check_overview.check_title_text()
        self.assertEqual('CHECKOUT: OVERVIEW', check_overview_text,
                         f'Expected login button text differ from actual: {check_overview_text}')# noqa
        check_overview.click_finish()

        # 9. check if checkout completed and back to home page
        check_complete_text = check_complete.check_title_text()
        self.assertEqual('THANK YOU FOR YOUR ORDER', check_complete_text,
                         f'Expected login button text differ from actual: {check_complete_text}')# noqa
        check_complete.back_home_page()

        # 10. log out
        burger_menu_page.log_out()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
