from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


def screenshot_and_broken_link_demo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        time.sleep(2)

        # 1. Take screenshot
        driver.save_screenshot("practice_page.png")
        print("Screenshot saved as 'practice_page.png'")

        # 2. Find the "Broken Link"
        broken_link = driver.find_element(By.LINK_TEXT, "Broken Link")
        link_url = broken_link.get_attribute("href")
        print(f"Link URL: {link_url}")

        #  3. Check the link status (ignore SSL warning)
        response = requests.get(link_url, verify=False)
        status_code = response.status_code
        print(f"Status Code: {status_code}")

        # 4. Verify
        if status_code == 404:
            print("The link is broken!")
        else:
            print("The link is valid.")

        time.sleep(2)

    finally:
        driver.quit()
        print("Browser closed successfully.")


screenshot_and_broken_link_demo()
