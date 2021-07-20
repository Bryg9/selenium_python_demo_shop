from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_CRED = (By.ID, 'login_credentials')
    LOGIN_INPUT = (By.XPATH, '//input[@placeholder="Username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Password"]')
    LOGIN_BTN = (By.ID, 'login-button')
    ALERT_CHECK = (By.XPATH, '//h3[@data-test="error"]')


class SaucePageLocators():
    TITLE_CHECK = (By.XPATH, '//span[@class="title"]')
    ADD_TSHIRT_BTN = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')# noqa
    CART_PRODUCT = (By.XPATH, '//a[@class="shopping_cart_link"]')


class HamburgerMenuLocators():
    HAMBURGER_MENU_BTN = (By.ID, 'react-burger-menu-btn')
    RESET_APP_STATE = (By.ID, 'reset_sidebar_link')
    CLOSE_MENU = (By.ID, 'react-burger-cross-btn')
    LOGOUT_BTN = (By.XPATH, '//a[@id="logout_sidebar_link"]')


class CartPageLocators():
    PRODUCT_TSHIRT_CHECK = (By.XPATH, '//div[@class="inventory_item_name"]')
    CHECKOUT_BTN = (By.ID, 'checkout')


class CartInfoPageLocators():
    PAGE_TITLE_CHECK = (By.XPATH, '//span[@class="title"]')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')


class CartOverwievPageLocators():
    OVERVIEW_TITLE_CHECK = (By.XPATH, '//span[@class="title"]')
    FINISH_BTN = (By.ID, 'finish')


class CartCompletePageLocators():
    COMPLETE_ORDER_CHECK = (By.XPATH, '//h2[@class="complete-header"]')
    BACK_HOME_BTN = (By.XPATH, '//button[@id="back-to-products"]')
