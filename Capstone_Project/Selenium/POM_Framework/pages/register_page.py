# pages/register_page.py
# Covers: radio buttons (gender), checkbox (newsletter), dropdowns (DOB), ids/names/xpaths

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RegisterPage:
    """Registration page with radio, checkbox, dropdowns."""
    URL = "https://demowebshop.tricentis.com/register"

    # --- Radio buttons (gender) ---
    GENDER_MALE = (By.ID, "gender-male")
    GENDER_FEMALE = (By.ID, "gender-female")

    # --- Text fields ---
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM = (By.ID, "ConfirmPassword")


    # --- Submit ---
    REGISTER_BTN = (By.ID, "register-button")
    RESULT = (By.CSS_SELECTOR, "div.result")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open register page."""
        self.driver.get(self.URL)

    def select_gender(self, gender="Male"):
        """Pick radio Male/Female."""
        if gender.lower().startswith("f"):
            self.driver.find_element(*self.GENDER_FEMALE).click()
        else:
            self.driver.find_element(*self.GENDER_MALE).click()

    def set_name_email(self, first, last, email):
        """Enter first/last/email."""
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def set_passwords(self, pwd):
        """Set password + confirm."""
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.CONFIRM).send_keys(pwd)



    def submit(self):
        """Click Register."""
        self.driver.find_element(*self.REGISTER_BTN).click()
