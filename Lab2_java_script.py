from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def lab4_javascript_scroll():
    # Step 1: Launch the browser and navigate to the site
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)
    print("Lab Exercise 4: JavaScriptExecutor for Scrolling ")

    # Step 2: Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled to the bottom of the page.")
    time.sleep(2)

    # Step 3: Scroll back to the top
    driver.execute_script("window.scrollTo(0, 0);")
    print("Scrolled back to the top of the page.")
    time.sleep(2)

    # Step 4: Find the “Mouse Hover” button
    mouse_hover_btn = driver.find_element(By.ID, "mousehover")

    # Step 5: Scroll until the button is in the viewport
    driver.execute_script("arguments[0].scrollIntoView();", mouse_hover_btn)
    print("Scrolled to the 'Mouse Hover' button.")
    time.sleep(2)

    # Step 6: Close the browser
    driver.quit()
    print(" Lab Exercise 4 Completed Successfully ")


# Run the program
lab4_javascript_scroll()
