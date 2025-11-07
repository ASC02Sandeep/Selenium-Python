from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def dropdown_demo_orangehrm():
    driver = webdriver.Chrome()

    try:
        # Open OrangeHRM and login
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # Go to Employee List page under PIM
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        time.sleep(4)

        # Select "Job Title" dropdown
        job_title_dropdown = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        job_title_dropdown.click()
        time.sleep(1)

        # Select one option (e.g., "Automation Tester")
        option = driver.find_element(By.XPATH, "//span[text()='Automation Tester']")
        option.click()
        print("Selected Job Title: Automation Tester")
        time.sleep(1)

        #  Select "Sub Unit" dropdown
        sub_unit_dropdown = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[3]")
        sub_unit_dropdown.click()
        time.sleep(1)

        # Choose "Engineering" as an example
        sub_unit_option = driver.find_element(By.XPATH, "//span[text()='Engineering']")
        sub_unit_option.click()
        print("Selected Sub Unit: Engineering")

        time.sleep(2)

    finally:
        driver.quit()
        print("Browser closed successfully.")


dropdown_demo_orangehrm()
