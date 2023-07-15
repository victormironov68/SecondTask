import pytest
from selenium.webdriver.common.by import By


def test_authorization(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.find_element()
