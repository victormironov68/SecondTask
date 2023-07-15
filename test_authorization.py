import pytest
from selenium.webdriver.common.by import By
import time


def test_authorization(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    time.sleep(3)

    login_button = browser.find_element(By.XPATH, "//*[@id='ember33']")
    login_button.click()

    time.sleep(3)

    email_field = browser.find_element(By.XPATH, "//*[@id='id_login_email']")
    email_field.send_keys("bart.68mail@gmail.com")

    password_field = browser.find_element(By.XPATH, "//*[@id='id_login_password']")
    password_field.send_keys("tuttyfrutty")

    input_button = browser.find_element(By.XPATH, "//*[@id='login_form']/button")
    input_button.click()



