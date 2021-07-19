import unittest
from tests.wrong_login_test import WrongCredentialsTest

# Load tests to run
wrong_credentials = unittest.TestLoader().loadTestsFromTestCase(WrongCredentialsTest)

# Create Test Suite
test_suite = unittest.TestSuite([wrong_credentials])

# run Test Suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
