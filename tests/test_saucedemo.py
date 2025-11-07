import pytest
import sys
import os

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage


class TestSauceDemo:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        yield driver

        driver.quit()

    def test_successful_login(self, driver):
        login_page = LoginPage()

        login_page.open(driver)

        login_page.login(driver, "standard_user", "secret_sauce")

        inventory_page = InventoryPage()

        # Assertion 1: Check URL contains inventory

        assert "inventory" in inventory_page.get_current_url(driver)

        # Assertion 2: Check page title is "Products"

        assert inventory_page.get_page_title(driver) == "Products"

        # Assertion 3: Check inventory items are displayed

        assert inventory_page.get_inventory_count(driver) > 0