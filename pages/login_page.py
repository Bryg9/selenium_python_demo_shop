from selenium.webdriver.chrome.webdriver import WebDriver
from pages.sauce_shop_main_page import SaucePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://www.saucedemo.com/'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def log_in_website_check(self):
        # check if login credentials are on page
        login_cred = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_CRED))# noqa
        print('You are on login page.', login_cred.is_displayed())

    def log_in(self, user, password):

        # type login in input box
        login_input = self.driver.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.click()
        login_input.send_keys(user)

        # type password in input box
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)# noqa
        password_input.click()
        password_input.send_keys(password)

        # click button 'Login'
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.click()

        return SaucePage(self.driver)

    def wrong_credentials_alert(self):
        alert = self.driver.find_element(*LoginPageLocators.ALERT_CHECK)
        return alert.text
