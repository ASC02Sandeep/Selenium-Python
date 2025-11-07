from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def multiple_elements_orangehrm():
    driver = webdriver.Chrome()

    try:
        # Open the OrangeHRM website
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)  # wait for page to load fully

        # Find all <a> tag elements (links)
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Total links found: {len(links)}")

        # Print first 10 links with visible text
        for i, link in enumerate(links[:10]):
            href = link.get_attribute("href")
            text = link.text.strip()
            if text:  # only print links with visible text
                print(f"{i + 1}. {text} -> {href}")

        # (Optional) Print social media icons if any
        print("\nPrinting all visible links completed successfully.")

    finally:
        driver.quit()
        print("Browser closed successfully.")


multiple_elements_orangehrm()
