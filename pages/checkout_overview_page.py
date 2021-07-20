from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CartOverwievPageLocators
from pages.checkout_complete_page import CartComplete


class CartOverview:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def check_title_text(self):
        messages_element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(CartOverwievPageLocators.OVERVIEW_TITLE_CHECK))# noqa
        return messages_element.text

    def click_finish(self):
        finish_btn = self.driver.find_element(*CartOverwievPageLocators.FINISH_BTN)# noqa
        finish_btn.click()

        return CartComplete(self.driver)
