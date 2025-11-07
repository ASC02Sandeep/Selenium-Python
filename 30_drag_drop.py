from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import time


def drag_drop_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/droppable")

        actions = ActionChains(driver)

        # Find source and target elements

        source = driver.find_element(By.ID, "draggable")

        target = driver.find_element(By.ID, "droppable")

        # Perform drag and drop

        actions.drag_and_drop(source, target).perform()

        time.sleep(2)

        # Verify drop

        target_text = target.text

        print(f"Target text after drop: {target_text}")



    finally:

        driver.quit()


drag_drop_demo()