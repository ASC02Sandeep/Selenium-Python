from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def orangehrm_hover_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)

        #  Login
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        print("Logged in successfully")

        actions = ActionChains(driver)

        #  Hover over "Admin" menu
        admin_menu = driver.find_element(By.XPATH, "//span[text()='Admin']")
        actions.move_to_element(admin_menu).perform()
        print("Hovered over 'Admin' menu")
        time.sleep(2)

        # Hover over "PIM" menu
        pim_menu = driver.find_element(By.XPATH, "//span[text()='PIM']")
        actions.move_to_element(pim_menu).perform()
        print("Hovered over 'PIM' menu")
        time.sleep(2)

        #  Hover over "Leave" menu
        leave_menu = driver.find_element(By.XPATH, "//span[text()='Leave']")
        actions.move_to_element(leave_menu).perform()
        print(" Hovered over 'Leave' menu")
        time.sleep(2)

    finally:
        driver.quit()
        print(" Browser closed")

orangehrm_hover_demo()
