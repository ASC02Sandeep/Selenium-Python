# tests/test_dashboard_screenshot.py
# Marks: smoke + ui → login → screenshot → title/text verification

import pytest
import os
from datetime import datetime
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@pytest.mark.ui
def test_login_and_capture_dashboard(driver, base_url):
    """Login → take screenshot → verify dashboard title or account name."""

    # ---------- LOGIN ----------
    login = LoginPage(driver)
    login.open()
    login.login("sandeep98@gmail.com", "sandeep123")

    assert login.is_logged_in(), " Login failed — cannot verify dashboard."

    # ---------- TAKE SCREENSHOT ----------
    folder = os.path.join(os.getcwd(), "screenshots")

    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(folder, f"dashboard_{timestamp}.png")

    driver.save_screenshot(file_path)
    print(f"\n Screenshot saved at: {file_path}")

    # ---------- VERIFY TEXT ON DASHBOARD ----------
    # After login, the account email appears at top right
    account_element = driver.find_element(By.CSS_SELECTOR, "a.account")
    account_text = account_element.text.strip()

    print(f" Logged-in account text: {account_text}")

    # assertion
    assert "@" in account_text, " Dashboard does not show account email."

    print(" Dashboard text assertion passed!")
