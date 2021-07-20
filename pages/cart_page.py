from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CartPageLocators
from pages.checkout_information_page import CartInfo


class CartPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.saucedemo.com/cart.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def check_product_in_cart(self):
        messages_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(CartPageLocators.PRODUCT_TSHIRT_CHECK))# noqa
        return messages_element.text

    def click_checkout(self):
        checkout = self.driver.find_element(*CartPageLocators.CHECKOUT_BTN)
        checkout.click()

        return CartInfo(self.driver)
