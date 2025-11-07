from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import time

def double_click_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/buttons")

        actions = ActionChains(driver)

        # Find the button for double click

        double_click_btn = driver.find_element(By.ID, "doubleClickBtn")

        # Perform double click

        actions.double_click(double_click_btn).perform()

        time.sleep(2)

        # Verify double click message

        message = driver.find_element(By.ID, "doubleClickMessage")

        print(f"Double click message: {message.text}")



    finally:

        driver.quit()


double_click_demo()