from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SaucePageLocators
from pages.cart_page import CartPage


class SaucePage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.saucedemo.com/inventory.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def get_messages_text(self):
        messages_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(SaucePageLocators.TITLE_CHECK))# noqa
        return messages_element.text

    def add_tshirt_to_cart(self):
        add_product_tshirt = self.driver.find_element(*SaucePageLocators.ADD_TSHIRT_BTN)# noqa
        add_product_tshirt.click()

        product_in_cart = self.driver.find_element(*SaucePageLocators.CART_PRODUCT)# noqa
        product_in_cart.click()

        return CartPage(self.driver)
