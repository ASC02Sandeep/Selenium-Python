# tests/test_registration.py
# Marks: ui + regression (uses radio, checkbox, dropdown, id/name/css/xpath)

import pytest
from pages.register_page import RegisterPage

@pytest.mark.ui
@pytest.mark.regression
def test_user_registration_flow(driver):
    """Register a user using radio/checkbox/dropdowns + assert success text."""
    page = RegisterPage(driver)
    page.open()

    # RADIO
    page.select_gender("Male")

    # TEXT + EMAIL (use unique email to avoid 'already exists')
    unique_email = f"nitin_{driver.session_id[:5]}@example.com"
    page.set_name_email("nitin", "Kumar", unique_email)

    # DROPDOWNS
    # page.set_dob(day="10", month="May", year="1995")

    # CHECKBOX (newsletter on registration form)
    # page.toggle_newsletter(True)

    # PASSWORDS
    page.set_passwords("nitin@123")

    # SUBMIT
    page.submit()

    # SIMPLE ASSERT using css (result div)
    result_text = driver.find_element(*RegisterPage.RESULT).text.lower()
    assert "completed" in result_text   # "Your registration completed"


#  NEW TEST ADDED WITH BUILT-IN MARKER (skip)
@pytest.mark.skip(reason="Drag-and-drop feature does not exist on Demo Web Shop")
def test_drag_and_drop_not_available():
    """
    This test is intentionally skipped.
    Demo Web Shop does NOT have any drag-and-drop functionality,
    but we include this test to demonstrate built-in skip marker usage.
    """
    assert False  # This will never run because test is skipped
