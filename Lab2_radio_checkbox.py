from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def lab2_checkbox_radio_demo():
    # Step 1: Launch the browser and navigate to the website
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Register.html")
    driver.maximize_window()
    time.sleep(2)


    # Step 2: Locate and click the "Male" radio button (using XPath)
    male_radio = driver.find_element(By.XPATH, "//input[@value='Male']")
    male_radio.click()
    time.sleep(1)

    # Step 3: Verify if "Male" radio button is selected
    is_male_selected = male_radio.is_selected()
    print(f"Male radio button selected: {is_male_selected}")

    # Step 4: Locate and click the "Cricket" checkbox
    cricket_checkbox = driver.find_element(By.XPATH, "//input[@value='Cricket']")
    cricket_checkbox.click()
    time.sleep(1)

    # Step 5: Locate and click the "Movies" checkbox
    movies_checkbox = driver.find_element(By.XPATH, "//input[@value='Movies']")
    movies_checkbox.click()
    time.sleep(1)

    # Step 6: Click "Movies" checkbox again to de-select it
    movies_checkbox.click()
    time.sleep(1)

    # Step 7: Verify selection status of both checkboxes
    print(f"Cricket checkbox selected: {cricket_checkbox.is_selected()}")
    print(f"Movies checkbox selected: {movies_checkbox.is_selected()}")

    # Step 8: Close the browser
    driver.quit()
    print(" Lab Exercise 2 Completed Successfully ")


# Run the demo
lab2_checkbox_radio_demo()
