from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def lab3_dropdown_demo():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Register.html")
    driver.maximize_window()
    time.sleep(5)  # Wait for page and dropdown to fully load


    # Step 2: "Skills" dropdown
    skills_dropdown = Select(driver.find_element(By.ID, "Skills"))
    skills_dropdown.select_by_visible_text("Adobe Photoshop")
    print("Selected 'Adobe Photoshop' from Skills dropdown.")
    time.sleep(1)

    # Step 3: "Country" dropdown
    country_dropdown = Select(driver.find_element(By.ID, "countries"))

    # Print all available countries to verify
    print("Available countries:")
    for option in country_dropdown.options:
        print(option.text)

    # Try to select Japan or fallback to another option
    try:
        country_dropdown.select_by_visible_text("Japan")
        print("Selected 'Japan' from Country dropdown.")
    except:
        if len(country_dropdown.options) > 1:
            country_dropdown.select_by_index(1)
            print("Japan not found — selected another country instead.")
        else:
            print("No countries available in dropdown.")
    time.sleep(1)

    # Step 4: "Year" dropdown
    year_dropdown = Select(driver.find_element(By.ID, "yearbox"))
    year_dropdown.select_by_index(5)
    print("Selected 5th option from Year dropdown.")
    time.sleep(1)

    # Step 5–6: Languages (custom dropdown)
    language_box = driver.find_element(By.ID, "msdd")
    language_box.click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[text()='English']").click()
    driver.find_element(By.XPATH, "//a[text()='French']").click()
    print("Selected English and French languages.")
    time.sleep(1)

    driver.find_element(By.XPATH, "//label[text()='Languages']").click()

    driver.quit()
    print("Lab Exercise 3 Completed Successfully ")


lab3_dropdown_demo()
