# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# def get_date_demo():
#     driver = webdriver.Chrome()
#
#     try:
#         driver.get("https://demoqa.com/automation-practice-form")
#         driver.maximize_window()
#         time.sleep(2)
#
#         # Locate the date input field
#         date_input = driver.find_element(By.ID, "dateOfBirthInput")
#
#         # Get and print the current date
#         current_value = date_input.get_attribute("value")
#         print(f"Current Date in the field: {current_value}")
#         time.sleep(2)
#
#         # Clear and set a new date
#         date_input.clear()
#         date_input.send_keys("10 Oct 2025")  # Format expected by site
#         time.sleep(1)
#
#         # Verify the updated date
#         new_value = date_input.get_attribute("value")
#         print(f"Updated Date in the field: {new_value}")
#
#     finally:
#         driver.quit()
#
# get_date_demo()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# def get_date_demo():
#     driver = webdriver.Chrome()
#
#     try:
#         # Open the page where the date field exists
#         driver.get("https://demoqa.com/automation-practice-form")
#         driver.maximize_window()
#         time.sleep(2)
#
#         # Locate the date input field
#         date_input = driver.find_element(By.ID, "dateOfBirthInput")
#
#         # Get and print the current date from the field
#         current_value = date_input.get_attribute("value")
#         print(f"Current Date in the field: {current_value}")
#         time.sleep(2)
#
#         #  Use JavaScript to change the date
#         driver.execute_script("arguments[0].value='10 Oct 2025';", date_input)
#         time.sleep(1)
#
#         # Verify the updated date
#         new_value = date_input.get_attribute("value")
#         print(f"Updated Date in the field: {new_value}")
#
#         time.sleep(2)
#
#     finally:
#         driver.quit()
#
# # Run the function
# get_date_demo()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_date_demo():
    driver = webdriver.Chrome()

    try:
        # Open the DemoQA form page
        driver.get("https://demoqa.com/automation-practice-form")
        driver.maximize_window()
        time.sleep(2)

        # Locate the date input field
        date_input = driver.find_element(By.ID, "dateOfBirthInput")

        # Print the current date
        current_value = date_input.get_attribute("value")
        print(f"Current Date in the field: {current_value}")
        time.sleep(1)

        # Clear the field using JavaScript first
        driver.execute_script("arguments[0].value='';", date_input)
        time.sleep(0.5)

        # Then set the new date value
        driver.execute_script("arguments[0].value='10 Oct 2025';", date_input)
        time.sleep(1)

        # Get the updated value
        new_value = date_input.get_attribute("value")
        print(f"Updated Date in the field: {new_value}")

        time.sleep(2)

    finally:
        driver.quit()

# Run the function
get_date_demo()


