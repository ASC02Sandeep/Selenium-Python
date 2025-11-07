from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def implicit_wait_demo():
    driver = webdriver.Chrome()

    # Set implicit wait (wait up to 10 seconds for elements)

    driver.implicitly_wait(10)

    try:

        driver.get("https://www.saucedemo.com")

        # These will wait up to 10 seconds if elements are not immediately found

        username = driver.find_element(By.ID, "user-name")

        password = driver.find_element(By.ID, "password")

        login_btn = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")

        password.send_keys("secret_sauce")

        login_btn.click()



    finally:

        driver.quit()


implicit_wait_demo()