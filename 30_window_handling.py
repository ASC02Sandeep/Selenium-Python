from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def window_handling_demo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://demoqa.com/browser-windows")

        # Store the parent window handle
        parent_window = driver.current_window_handle
        print(f"Parent window: {parent_window}")

        # Click button to open new window
        new_window_btn = driver.find_element(By.ID, "windowButton")
        new_window_btn.click()
        time.sleep(2)

        # Get all window handles
        all_windows = driver.window_handles
        print(f"Total windows: {len(all_windows)}")

        # Switch to new window
        for window in all_windows:

            if window != parent_window:
                driver.switch_to.window(window)
                print(f"Switched to: {driver.current_window_handle}")
                print(f"New window title: {driver.title}")
                print(f"New window URL: {driver.current_url}")

                # Do something in new window

                text_element = driver.find_element(By.TAG_NAME, "body")
                print(f"New window content: {text_element.text}")

                # Close new window

                driver.close()

                break

                # Switch back to parent window

        driver.switch_to.window(parent_window)
        print(f"Back to parent: {driver.title}")

    finally:
        driver.quit()

window_handling_demo()