# pages/login_page.py
# Covers: id/name/css, explicit waits, success (account link) and failure (validation summary)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Login page: login + helpers to verify success/failure."""
    URL = "https://demowebshop.tricentis.com/login"

    # --- Locators ---
    EMAIL = (By.ID, "Email")                                  # by ID
    PASSWORD = (By.NAME, "Password")                          # by NAME
    LOGIN_BTN = (By.CSS_SELECTOR, "input.button-1.login-button")
    VALIDATION_SUMMARY = (By.CSS_SELECTOR, "div.validation-summary-errors")  # <== restored
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a.account")             # appears on success (top link with email)

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the login page and wait until the email field is present."""
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EMAIL)
        )

    def login(self, email: str, pwd: str):
        """Fill credentials and submit."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EMAIL)
        )
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def is_logged_in(self) -> bool:
        """Return True if account link becomes visible after login."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ACCOUNT_LINK)
            )
            return True
        except Exception:
            return False

    def error_text(self) -> str:
        """If login failed, return validation summary text (empty if not present)."""
        try:
            el = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.VALIDATION_SUMMARY)
            )
            return el.text or ""
        except Exception:
            return ""


# # pages/login_page.py
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class LoginPage:
#     """Login page: login + helper to verify login success."""
#     URL = "https://demowebshop.tricentis.com/login"
#
#     EMAIL = (By.ID, "Email")
#     PASSWORD = (By.NAME, "Password")
#     LOGIN_BTN = (By.CSS_SELECTOR, "input.button-1.login-button")
#     ACCOUNT_LINK = (By.CSS_SELECTOR, "a.account")
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def open(self):
#         """Open login page and wait until Email field appears."""
#         self.driver.get(self.URL)
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.EMAIL)
#         )
#
#     def login(self, email, pwd):
#         """Fill credentials and submit."""
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.EMAIL)
#         )
#
#         self.driver.find_element(*self.EMAIL).clear()
#         self.driver.find_element(*self.EMAIL).send_keys(email)
#         self.driver.find_element(*self.PASSWORD).clear()
#         self.driver.find_element(*self.PASSWORD).send_keys(pwd)
#         self.driver.find_element(*self.LOGIN_BTN).click()
#
#     def is_logged_in(self):
#         """Return True if account link is visible after login."""
#         try:
#             WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located(self.ACCOUNT_LINK)
#             )
#             return True
#         except:
#             return False
#
#
# # # pages/login_page.py
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # class LoginPage:
# #     """Login page: login + helper to verify login success."""
# #     URL = "https://demowebshop.tricentis.com/login"
# #
# #     EMAIL = (By.ID, "Email")
# #     PASSWORD = (By.NAME, "Password")
# #     LOGIN_BTN = (By.CSS_SELECTOR, "input.button-1.login-button")
# #     ACCOUNT_LINK = (By.CSS_SELECTOR, "a.account")
# #
# #     def __init__(self, driver):
# #         self.driver = driver
# #
# #     def open(self):
# #         """Open login page and wait until Email field appears."""
# #         self.driver.get(self.URL)
# #
# #         # ✅ wait for Email field to be present
# #         WebDriverWait(self.driver, 10).until(
# #             EC.presence_of_element_located(self.EMAIL)
# #         )
# #
# #     def login(self, email, pwd):
# #         """Fill credentials and submit."""
# #         WebDriverWait(self.driver, 10).until(
# #             EC.presence_of_element_located(self.EMAIL)
# #         )
# #
# #         self.driver.find_element(*self.EMAIL).clear()
# #         self.driver.find_element(*self.EMAIL).send_keys(email)
# #         self.driver.find_element(*self.PASSWORD).clear()
# #         self.driver.find_element(*self.PASSWORD).send_keys(pwd)
# #         self.driver.find_element(*self.LOGIN_BTN).click()
# #
# #     def is_logged_in(self):
# #         """Return True if account link is visible after login."""
# #         try:
# #             WebDriverWait(self.driver, 5).until(
# #                 EC.presence_of_element_located(self.ACCOUNT_LINK)
# #             )
# #             return True
# #         except:
# #             return False
