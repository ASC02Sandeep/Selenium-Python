# tests_lab/test_form_validation.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytest_lab.src_lab.form_page import FormPage


@pytest.fixture
def driver():
    """Browser fixture"""
    options = Options()
    # options.add_argument("--headless")  # run browser visibly; uncomment for headless
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.mark.selenium
def test_required_field_validation(driver):
    """Submit without entering required data → should NOT submit form."""
    page = FormPage(driver)
    page.load()
    page.submit_form()

    assert not page.is_submission_successful()


@pytest.mark.selenium
def test_email_format_validation(driver):
    """Invalid email should fail validation."""
    page = FormPage(driver)
    page.load()
    page.fill_form("John", "Doe", "wrong-email-format")
    page.submit_form()

    assert page.get_email_field_error() is True
    assert not page.is_submission_successful()


@pytest.mark.selenium
def test_successful_form_submission(driver):
    """Valid form should submit successfully."""
    page = FormPage(driver)
    page.load()
    page.fill_form("Alice", "Smith", "alice.smith@gmail.com")
    page.submit_form()

    assert page.is_submission_successful() is True
