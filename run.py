import unittest
from tests.login_page_test import LoginPageTest
from tests.buy_product_test import BuyProductTest
from tests.wrong_login_test import WrongCredentialsTest

# Load tests to run
wrong_credentials = unittest.TestLoader().loadTestsFromTestCase(WrongCredentialsTest)
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
buy_product = unittest.TestLoader().loadTestsFromTestCase(BuyProductTest)

# Create Test Suite
test_suite = unittest.TestSuite([wrong_credentials, login_test, buy_product])

# run Test Suite
unittest.TextTestRunner(verbosity=2).run(test_suite)