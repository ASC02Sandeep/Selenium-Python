from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def explicit_wait_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        # Click the start button
        start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
        start_button.click()
        print("Clicked Start button")

        # Wait explicitly for the text to appear
        wait = WebDriverWait(driver, 10)
        finish_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
        )

        print("Text appeared:", finish_text.text)

    finally:
        driver.quit()

explicit_wait_demo()
