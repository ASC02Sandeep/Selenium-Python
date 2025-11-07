from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeLoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/"
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, driver):
        driver.get(self.URL)

    def enter_username(self, driver, username):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).send_keys(username)

    def enter_password(self, driver, password):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        ).send_keys(password)

    def click_login(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, driver, username, password):
        self.enter_username(driver, username)
        self.enter_password(driver, password)
        self.click_login(driver)
