
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """Page Object Model for DemoQA Form"""

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        self.first_name = (By.ID, "firstName")
        self.last_name = (By.ID, "lastName")
        self.email = (By.ID, "userEmail")
        self.gender_male = (By.XPATH, "//label[text()='Male']")
        self.password = (By.ID, "userNumber")   # We'll simulate password field using phone number
        self.submit = (By.ID, "submit")
        self.modal_title = (By.ID, "example-modal-sizes-title-lg")

    def load(self):
        self.driver.get(self.url)

    def fill_form(self, fname, lname, email):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.gender_male).click()

    # def submit_form(self):
    #     self.driver.find_element(*self.submit).click()

    def submit_form(self):
        submit_btn = self.driver.find_element(*self.submit)

        # Scroll the button into view (fixes intercepted click issue)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)

        # Small wait to ensure position stabilizes
        import time
        time.sleep(0.5)

        submit_btn.click()

    def is_submission_successful(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.modal_title)
            )
            return True
        except:
            return False

    def get_email_field_error(self):
        # email field turns red if invalid → detect "field-error" class
        email_field = self.driver.find_element(*self.email)
        return "field-error" in email_field.get_attribute("class")
