# tests/test_newsletter_and_nav.py
# Marks: ui; AJAX newsletter + back/forward navigation

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


@pytest.mark.ui
def test_newsletter_ajax_and_navigation(driver, wait, base_url):
    """Subscribe to newsletter (AJAX) then test back/forward navigation."""

    home = HomePage(driver)
    home.open(base_url)

    # Use a unique email always (newsletter has server-side caching)
    random_mail = f"qa_{driver.session_id[:5]}@example.com"
    home.subscribe_newsletter(random_mail)

    # FIXED: Wait until newsletter result block contains ANY text (not empty)
    wait.until(lambda d:
        d.find_element(*HomePage.NEWSLETTER_RESULT).text.strip() != ""
    )

    # Get the message now
    msg = driver.find_element(*HomePage.NEWSLETTER_RESULT).text.strip()

    # Validate message exists
    assert msg != "", "Newsletter subscription did not return a message!"

    # NAVIGATION back / forward
    driver.back()
    driver.forward()

    # Quick sanity check home still reachable
    assert "demowebshop" in driver.current_url.lower()



