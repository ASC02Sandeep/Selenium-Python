from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def screenshot_demo_orangehrm():
    driver = webdriver.Chrome()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)  # wait for page to fully load

        # Create screenshots folder if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # Take screenshot of the login page
        driver.save_screenshot("screenshots/login_page.png")
        print("Login page screenshot saved")

        #  Perform login
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()
        time.sleep(3)

        # Take screenshot after login (Dashboard)
        driver.save_screenshot("screenshots/after_login.png")
        print("After login screenshot saved")

        #  Take screenshot of specific element (Dashboard logo)
        dashboard_logo = driver.find_element(By.XPATH, "//img[@alt='client brand banner']")
        dashboard_logo.screenshot("screenshots/specific_element.png")
        print("Specific element screenshot saved")

    finally:
        driver.quit()
        print("Browser closed successfully.")


screenshot_demo_orangehrm()
