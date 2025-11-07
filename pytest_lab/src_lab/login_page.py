
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object for SauceDemo login page."""

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        """Open the login page."""
        self.driver.get(self.url)

    def login(self, username, password):
        """Perform login using given credentials."""
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """Return login error message text."""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_message)
            )
            return element.text
        except Exception:
            return None

    def is_logged_in(self):
        """Check if user redirected to inventory page after login."""
        WebDriverWait(self.driver, 5).until(EC.url_contains("inventory.html"))
        return "inventory.html" in self.driver.current_url
