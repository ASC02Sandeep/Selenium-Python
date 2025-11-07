from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def frame_handling_demo():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()

    try:
        # Step 1: Switch to the iframe by ID
        driver.switch_to.frame("mce_0_ifr")
        print("Switched to the iframe")

        # Step 2: Locate the editable body
        text_box = driver.find_element(By.ID, "tinymce")

        # Step 3: Use JavaScript to clear content instead of clear()
        driver.execute_script("arguments[0].innerHTML = '';", text_box)
        print("Cleared text inside the iframe")

        # Step 4: Send new text
        text_box.send_keys("Hello from Selenium inside an iframe!")
        print("New text entered inside the iframe")

        # Step 5: Switch back to main content
        driver.switch_to.default_content()
        print("Switched back to main content")

        # Step 6: Verify heading on main page
        header_text = driver.find_element(By.TAG_NAME, "h3").text
        print("Main page header:", header_text)

    finally:
        time.sleep(2)
        driver.quit()

frame_handling_demo()
