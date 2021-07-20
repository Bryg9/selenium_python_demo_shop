from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CartCompletePageLocators


class CartComplete:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def check_title_text(self):
        messages_element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(CartCompletePageLocators.COMPLETE_ORDER_CHECK))# noqa
        return messages_element.text

    def back_home_page(self):
        finish_btn = self.driver.find_element(*CartCompletePageLocators.BACK_HOME_BTN)# noqa
        finish_btn.click()
