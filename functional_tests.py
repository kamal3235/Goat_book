"""Functional tests using Selenium and Django."""

from selenium import webdriver


browser = webdriver.Firefox()
browser.get("http://localhost: 8000")

assert "Congratulation!" in browser.title
print("Ok")
