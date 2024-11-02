"""Functional tests using Selenium and Django."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute(
            "placeholder"), "Enter a to-do item")

        inputbox.send_keys("Buy peacock feathers")

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows),
            "New to-do item did not appear in table",
        )

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

# """
#  (.venv) C:\Users\kamal\goat_book>python functional_tests.py
# F
# ======================================================================
# FAIL: test_can_start_a_todo_list (__main__.NewVisitorTest.test_can_start_a_todo_list)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\kamal\goat_book\functional_tests.py", line 17, in test_can_start_a_todo_list
#     self.assertIn("To-Do", self.browser.title)
#     ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError: 'To-Do' not found in 'The install worked successfully! Congratulations!'

# ----------------------------------------------------------------------
# Ran 1 test in 8.558s

# FAILED (failures=1)

# (.venv) C:\Users\kamal\goat_book>
# """
