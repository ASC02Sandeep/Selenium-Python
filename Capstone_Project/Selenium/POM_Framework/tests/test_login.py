# tests/test_login.py
# Marks: smoke + login; also shows explicit wait

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from pages.login_page import LoginPage
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.login
def test_login_invalid(driver, wait):
    """Invalid login shows validation summary (explicit wait)."""
    page = LoginPage(driver)
    page.open()
    page.login("invalid@example.com", "wrongpass")

    # EXPLICIT WAIT: validation summary appears
    elem = wait.until(EC.visibility_of_element_located(LoginPage.VALIDATION_SUMMARY))
    assert "login was unsuccessful" in elem.text.lower()

@pytest.mark.login
def test_login_then_logout_menu(driver, wait, base_url):
    """Small valid login (if you have a known account) + menu hover (action)."""
    page = LoginPage(driver)
    page.open()
    # NOTE: replace with your real creds if you want to actually pass this
    # page.login("someone@valid.com", "ValidPass123")
    page.login("sandeep98@gmail.com", "sandeep123")

    # Either account link appears or stays on login
    try:
        acc = wait.until(EC.visibility_of_element_located(LoginPage.ACCOUNT_LINK))
        assert "@" in acc.text
    finally:
        # Navigate back home whether pass/fail to keep consistent
        driver.get(base_url)
