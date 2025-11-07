from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def window_handling_demo():
    driver = webdriver.Chrome()

    try:
        # Step 1: Open the page
        driver.get("https://the-internet.herokuapp.com/windows")

        # Step 2: Store parent window handle
        parent_window = driver.current_window_handle
        print(f"Parent window handle: {parent_window}")

        # Step 3: Click link to open a new window
        link = driver.find_element(By.LINK_TEXT, "Click Here")
        link.click()
        time.sleep(2)  # Just for observation

        # Step 4: Get all window handles
        all_windows = driver.window_handles
        print(f"Total windows: {len(all_windows)}")

        # Step 5: Switch to the new window
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print(f"Switched to: {driver.current_window_handle}")
                print(f"New window title: {driver.title}")
                print(f"New window URL: {driver.current_url}")

                # Step 6: Print content of new window
                text_element = driver.find_element(By.TAG_NAME, "h3")
                print(f"New window content: {text_element.text}")

                # Step 7: Close new window
                driver.close()
                break

        # Step 8: Switch back to parent window
        driver.switch_to.window(parent_window)
        print(f"Back to parent window title: {driver.title}")

    finally:
        driver.quit()

window_handling_demo()
