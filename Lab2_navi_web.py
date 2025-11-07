from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def lab1_navigation_demo():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Index.html")
    driver.maximize_window()
    time.sleep(2)

    # Click "Skip Sign In"
    skip_sign_in = driver.find_element(By.ID, "btn2")
    skip_sign_in.click()
    time.sleep(3)  # Give time for page to load fully

    # Fill in form fields
    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name.send_keys("Sandeep")

    last_name = driver.find_element(By.XPATH, "//input[@ng-model='LastName']")
    last_name.send_keys("Kumar")

    address = driver.find_element(By.XPATH, "//textarea[@rows='3']")
    address.send_keys("123 Main Street, Hyderabad")

    # Get and print header text
    header = driver.find_element(By.TAG_NAME, "h1")
    print(f"Page Header Text: {header.text}")

    # Go back to Index page
    driver.back()
    time.sleep(2)

    driver.quit()


lab1_navigation_demo()
