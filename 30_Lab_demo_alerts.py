from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def simple_alert_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # Simple Alert
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = driver.switch_to.alert
        print("Alert text:", alert.text)
        alert.accept()
        print("Simple alert accepted")

        time.sleep(1)

        #  Confirmation Alert
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = driver.switch_to.alert
        print("Confirm text:", alert.text)
        alert.dismiss()
        print(" Confirmation alert dismissed")

        time.sleep(1)

        # Prompt Alert
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = driver.switch_to.alert
        alert.send_keys("Selenium Python")
        print("Text entered in prompt")
        alert.accept()
        print(" Prompt alert accepted")

        time.sleep(2)

    finally:
        driver.quit()

simple_alert_demo()
