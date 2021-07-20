from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HamburgerMenuLocators
from locators import LoginPageLocators
import time


class HamburgerMenuPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def reset_app_state(self):
        # reset app state
        burger_menu = self.driver.find_element(*HamburgerMenuLocators.HAMBURGER_MENU_BTN)# noqa
        burger_menu.click()
        time.sleep(2)
        reset_state = self.driver.find_element(*HamburgerMenuLocators.RESET_APP_STATE)# noqa
        reset_state.click()
        close_burger_menu = self.driver.find_element(*HamburgerMenuLocators.CLOSE_MENU)# noqa
        close_burger_menu.click()

    def log_out(self):
        burger_menu = self.driver.find_element(*HamburgerMenuLocators.HAMBURGER_MENU_BTN)# noqa
        burger_menu.click()
        logout_btn = self.driver.find_element(*HamburgerMenuLocators.LOGOUT_BTN)# noqa
        logout_btn.click()
        logout_check = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_CRED))# noqa
        print('You are logged out.', logout_check.is_displayed())
