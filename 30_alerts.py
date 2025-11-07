from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def alerts_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://demoqa.com/alerts")
        # remove annoying ads/banners
        driver.execute_script("document.querySelector('#fixedban')?.remove();")
        driver.execute_script("document.querySelectorAll('iframe').forEach(a => a.remove());")

        # 1. Simple Alert
        simple_alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", simple_alert_btn)
        simple_alert_btn.click()

        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()
        print("Simple alert accepted")

        # 2. Confirmation Alert
        confirm_alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "confirmButton")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_alert_btn)
        confirm_alert_btn.click()

        alert = driver.switch_to.alert
        print(f"Confirm alert text: {alert.text}")
        alert.dismiss()
        print("Confirmation alert dismissed")

        # 3. Prompt Alert
        prompt_alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "promtButton")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", prompt_alert_btn)
        prompt_alert_btn.click()

        alert = driver.switch_to.alert
        alert.send_keys("Selenium Python")
        print("Text entered in prompt")
        alert.accept()
        print("Prompt alert accepted")

        time.sleep(2)

    finally:
        driver.quit()

alerts_demo()
