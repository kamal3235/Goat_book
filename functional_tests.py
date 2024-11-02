"""Functional tests using Selenium and Django."""

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        [...]


# browser = webdriver.Firefox()

# browser.get("http://localhost: 8000")

# assert "To-Do" in browser.title

# browser.quit()

# assert "Congratulation!" in browser.title
# print("Ok")

if __name__ == "__main__":
    unittest.main()

# Python script checks if it’s been executed from the command line,
# rather than just imported by another script
# output
"""
 (.venv) C:\Users\kamal\goat_book>python functional_tests.py
F
======================================================================
FAIL: test_can_start_a_todo_list (__main__.NewVisitorTest.test_can_start_a_todo_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\kamal\goat_book\functional_tests.py", line 17, in test_can_start_a_todo_list
    self.assertIn("To-Do", self.browser.title)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'To-Do' not found in 'The install worked successfully! Congratulations!'

----------------------------------------------------------------------
Ran 1 test in 8.558s

FAILED (failures=1)

(.venv) C:\Users\kamal\goat_book>   
"""
