from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def double_click_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()

        actions = ActionChains(driver)

        # Locate double-click button
        double_click_btn = driver.find_element(By.XPATH, "//button[text()='Copy Text']")

        # Perform double-click
        actions.double_click(double_click_btn).perform()
        time.sleep(2)

        # Verify effect (text copied to input field)
        copied_text = driver.find_element(By.ID, "field2").get_attribute("value")
        print(f"Text copied after double click: {copied_text}")

    finally:
        driver.quit()


double_click_demo()
