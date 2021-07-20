from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CartInfoPageLocators
from pages.checkout_overview_page import CartOverview


class CartInfo:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.saucedemo.com/checkout-step-one.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def check_title_text(self):
        messages_element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(CartInfoPageLocators.PAGE_TITLE_CHECK))# noqa
        return messages_element.text

    def fill_personal_data(self, first_name, last_name, postal_code):
        firstName = self.driver.find_element(*CartInfoPageLocators.FIRST_NAME)
        firstName.send_keys(first_name)

        lastName = self.driver.find_element(*CartInfoPageLocators.LAST_NAME)
        lastName.send_keys(last_name)

        postalCode = self.driver.find_element(*CartInfoPageLocators.POSTAL_CODE)# noqa
        postalCode.send_keys(postal_code)

        continue_btn = self.driver.find_element(*CartInfoPageLocators.CONTINUE_BTN)# noqa
        continue_btn.click()

        return CartOverview(self.driver)
