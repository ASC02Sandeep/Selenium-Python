#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from pytest_lab.src_lab.login_page import LoginPage
#
# @pytest.fixture
# def driver():
#     """Fixture to set up and tear down the WebDriver."""
#     options = Options()
#     options.add_argument("--headless")  # Run tests without opening a window
#     service = Service()  # uses default chromedriver on PATH
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
#
#
# @pytest.mark.selenium
# def test_successful_login(driver):
#     """Verify successful login with valid credentials."""
#     page = LoginPage(driver)
#     page.load()
#     page.login("standard_user", "secret_sauce")
#
#     assert page.is_logged_in()
#     assert "inventory.html" in driver.current_url
#
#
# @pytest.mark.selenium
# def test_login_failure_invalid_credentials(driver):
#     """Verify error message with invalid credentials."""
#     page = LoginPage(driver)
#     page.load()
#     page.login("wrong_user", "wrong_pass")
#
#     error = page.get_error_message()
#     assert error is not None
#     assert "Epic sadface" in error
#
#
# @pytest.mark.selenium
# def test_error_message_text(driver):
#     """Check error message assertion explicitly."""
#     page = LoginPage(driver)
#     page.load()
#     page.login("locked_out_user", "secret_sauce")
#
#     error = page.get_error_message()
#     assert "Sorry, this user has been locked out." in error
#
#
# @pytest.mark.selenium
# def test_page_redirection_after_login(driver):
#     """Validate that user is redirected after successful login."""
#     page = LoginPage(driver)
#     page.load()
#     page.login("standard_user", "secret_sauce")
#
#     assert page.is_logged_in()
#     assert "inventory.html" in driver.current_url



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytest_lab.src_lab.login_page import LoginPage


@pytest.fixture
def driver():
    """Fixture to set up and tear down the WebDriver."""
    options = Options()
    # options.add_argument("--headless")  # Commented: run with visible browser window
    service = Service()  # Uses default ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.mark.selenium
def test_successful_login(driver):
    """Verify successful login with valid credentials."""
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "secret_sauce")

    assert page.is_logged_in()
    assert "inventory.html" in driver.current_url


@pytest.mark.selenium
def test_login_failure_invalid_credentials(driver):
    """Verify error message with invalid credentials."""
    page = LoginPage(driver)
    page.load()
    page.login("wrong_user", "wrong_pass")

    error = page.get_error_message()
    assert error is not None
    assert "Epic sadface" in error


@pytest.mark.selenium
def test_error_message_text(driver):
    """Check error message assertion explicitly."""
    page = LoginPage(driver)
    page.load()
    page.login("locked_out_user", "secret_sauce")

    error = page.get_error_message()
    assert "Sorry, this user has been locked out." in error


@pytest.mark.selenium
def test_page_redirection_after_login(driver):
    """Validate that user is redirected after successful login."""
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "secret_sauce")

    assert page.is_logged_in()
    assert "inventory.html" in driver.current_url

