import pytest
import os
import sys
from selenium import webdriver

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.orange_login_page import OrangeLoginPage
from pages.orange_dashboard_page import OrangeDashboardPage

class TestOrangeHRM:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        login_page = OrangeLoginPage()
        dashboard_page = OrangeDashboardPage()

        login_page.open(driver)
        login_page.login(driver, "Admin", "admin123")

        assert dashboard_page.is_dashboard_displayed(driver)
        print("Login successful and dashboard is visible.")
