from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def implicit_wait_alert_demo():
    driver = webdriver.Chrome()

    # Implicit wait: waits up to 10 seconds for elements
    driver.implicitly_wait(10)

    try:
        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

        # Simple Alert
        driver.find_element(By.ID, "alertexamples").click()
        alert = driver.switch_to.alert
        print("Alert text:", alert.text)
        alert.accept()
        print(" Simple alert accepted")

        time.sleep(1)

        #  Confirmation Alert
        driver.find_element(By.ID, "confirmexample").click()
        alert = driver.switch_to.alert
        print("Confirm alert text:", alert.text)
        alert.dismiss()
        print(" Confirmation alert dismissed")

        time.sleep(1)

        #  Prompt Alert
        driver.find_element(By.ID, "promptexample").click()
        alert = driver.switch_to.alert
        alert.send_keys("Selenium Python")
        print(" Text entered in prompt")
        alert.accept()
        print("Prompt alert accepted")

        time.sleep(1)

    finally:
        driver.quit()

implicit_wait_alert_demo()
