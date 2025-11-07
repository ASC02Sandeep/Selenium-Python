import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.selenium
def test_checkbox_toggle_states(driver):
    driver.get("https://demoqa.com/checkbox")

    # Expand tree and toggle checkbox
    expand_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_button.click()

    checkbox = driver.find_element(By.CSS_SELECTOR, "span.rct-title")
    checkbox.click()

    # Verify result message shows checkbox selected
    result = driver.find_element(By.ID, "result").text.lower()
    assert "home" in result


@pytest.mark.selenium
def test_bulk_selection(driver):
    driver.get("https://demoqa.com/checkbox")

    # Click expand all
    driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']").click()

    # Click select all (the main checkbox)
    driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-home']").click()

    result = driver.find_element(By.ID, "result").text.lower()

    # Verify multiple items selected
    assert "desktop" in result and "documents" in result and "downloads" in result


@pytest.mark.selenium
def test_radio_button_exclusivity(driver):
    driver.get("https://demoqa.com/radio-button")

    yes_radio = driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
    impressive_radio = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")

    yes_radio.click()
    result = driver.find_element(By.CLASS_NAME, "text-success").text
    assert result == "Yes"

    impressive_radio.click()
    result = driver.find_element(By.CLASS_NAME, "text-success").text
    assert result == "Impressive"


@pytest.mark.selenium
def test_required_field_marking(driver):
    driver.get("https://demoqa.com/radio-button")

    # The "No" option is disabled
    no_radio = driver.find_element(By.ID, "noRadio")
    assert not no_radio.is_enabled(), "The 'No' option should be disabled (required field behavior)"




