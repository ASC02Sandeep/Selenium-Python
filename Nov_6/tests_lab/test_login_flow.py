import pytest
from Nov_6.src_lab.pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


@pytest.mark.login
@pytest.mark.regression
def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wrong", "wrong")
    assert "do not match" in page.get_error()
