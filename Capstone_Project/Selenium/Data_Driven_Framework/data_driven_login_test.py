import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class DemoWebShopLoginTest:

    def __init__(self):
        self.driver = None
        self.excel_file = "test_data/login_data.xlsx"

    def setup_browser(self, headless=False):
        """Launch browser and open Demo Web Shop login page"""

        from selenium.webdriver.chrome.options import Options
        myoptions = Options()

        if headless:
            myoptions.add_argument("--headless")
            myoptions.add_argument("--disable-gpu")
            myoptions.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=myoptions)
        self.driver.maximize_window()
        self.driver.get("https://demowebshop.tricentis.com/login")
        time.sleep(2)

    def read_test_data(self):
        """Read login test cases from Excel"""
        workbook = openpyxl.load_workbook(self.excel_file)
        sheet = workbook["LoginTests"]

        test_cases = []
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0]:  # skip empty rows
                test_cases.append(dict(zip(headers, row)))

        workbook.close()
        return test_cases

    def perform_login(self, username, password):
        """Perform login and return result"""
        email_field = self.driver.find_element(By.ID, "Email")
        password_field = self.driver.find_element(By.ID, "Password")
        login_button = self.driver.find_element(By.XPATH, "//input[@value='Log in']")

        email_field.clear()
        password_field.clear()

        if username:
            email_field.send_keys(username)
        if password:
            password_field.send_keys(password)

        login_button.click()
        time.sleep(3)

        # success check → after login logout link is visible
        if "logout" in self.driver.page_source.lower():
            return "Success"
        else:
            return "Error"

    def logout_if_logged_in(self):
        """Logout if login was successful"""
        if "logout" in self.driver.page_source.lower():
            self.driver.find_element(By.LINK_TEXT, "Log out").click()
            time.sleep(2)

    def run_tests(self):
        self.setup_browser()
        test_cases = self.read_test_data()
        passed = 0

        print("\nEXECUTING DATA DRIVEN LOGIN TESTS\n")

        for case in test_cases:
            print(f"Running: {case['TestCaseID']} -> {case['Username']}")
            actual = self.perform_login(case['Username'], case['Password'])

            if actual == case['ExpectedResult']:
                print("  ✓ PASS")
                passed += 1
            else:
                print("  ✗ FAIL")

            self.logout_if_logged_in()
            self.driver.get("https://demowebshop.tricentis.com/login")

        total = len(test_cases)
        print("\nTEST SUMMARY")
        print(f"Total: {total}, Passed: {passed}, Failed: {total - passed}")

        self.driver.quit()


if __name__ == "__main__":
    DemoWebShopLoginTest().run_tests()
