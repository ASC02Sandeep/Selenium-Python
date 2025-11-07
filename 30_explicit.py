from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time


def explicit_wait_demo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com")

        # Login first

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Use explicit wait for specific condition
        wait = WebDriverWait(driver, 10)

        # Wait for products to be visible
        products = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        print("Products are visible")

        # Wait for element to be clickable
        product_item = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name"))
        )
        product_item.click()
        print("Product clicked")

        # Wait for URL to contain specific text
        wait.until(EC.url_contains("inventory-item"))
        print("Navigated to product details")


    finally:
        driver.quit()

explicit_wait_demo()