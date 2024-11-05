"""Functional tests using Selenium and Django."""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os


MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        test_server = os.environ.get("TEST_SERVER")
        if test_server:
            self.live_server_url = "http://" + test_server

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)

        # inputbox.send_keys(Keys.ENTER)
        # # time.sleep(1)
        # self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # inputbox = self.browser.find_element(By.ID, "id_new_item")
        # inputbox.send_keys("Use peacock feathers to make a fly")
        # inputbox.send_keys(Keys.ENTER)
        # # time.sleep(1)

        # self.wait_for_row_in_list_table("1: Buy peacock feathers")
        # self.wait_for_row_in_list_table(
        #     "2: Use peacock feathers to make a fly")

        # self.check_for_row_in_list_table("1: Buy peacock feathers")
        # self.check_for_row_in_list_table(
        #     "2: Use peacock feathers to make a fly")

    def test_can_start_a_todo_list(self):
        self.browser.get(self.live_server_url)
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")

        self.browser.delete_all_cookies()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(inputbox.location["x"] + inputbox.size["width"] / 2,
                               512,
                               delta=10,
                               )

        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: testing")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2,
            512,
            delta=10
        )

        # enter a to-do item
        # inputbox = self.browser.find_element(By.ID, "id_new_item")
        # inputbox.send_keys("Use peacock feathers to make a fly")
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # self.check_for_row_in_list_table("1: Buy peacock feathers")

        # inputbox = self.browser.find_element(By.ID, "id_new_item")
        # inputbox.send_keys("Use peacock feathers to make a fly")
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # self.check_for_row_in_list_table("1: Buy peacock feathers")
        # self.check_for_row_in_list_table(
        #     "2: Use peacock feathers to make a fly")

        # table = self.browser.find_element(By.ID, "id_list_table")
        # rows = table.find_elements(By.TAG_NAME, "tr")
        # self.assertIn(
        #     "1: Buy peacock feathers",
        #     [row.text for row in rows]
        # )

        # self.assertIn(
        #     "2: Use peacock feathers to make a fly",
        #     [row.text for row in rows]
        # )

        # self.assertTrue(
        #     any(row.text == "1: Buy peacock feathers" for row in rows),
        #     f"New to-do item did not appear in table. Contents were:\n{
        #         table.text}",
        # )

        # self.fail("Finish the test!")


# browser = webdriver.Firefox()

# browser.get("http://localhost: 8000")

# assert "To-Do" in browser.title

# browser.quit()

# assert "Congratulation!" in browser.title
# print("Ok")

# if __name__ == "__main__":
#     unittest.main()

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
