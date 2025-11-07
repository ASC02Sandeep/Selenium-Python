import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.selenium
def test_default_selected_option(driver):
    driver.get("https://demoqa.com/select-menu")

    # Locate old-style dropdown
    dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))

    # Verify default selected option
    assert dropdown.first_selected_option.text == "Red"


@pytest.mark.selenium
def test_all_available_options(driver):
    driver.get("https://demoqa.com/select-menu")

    dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
    options = [opt.text for opt in dropdown.options]

    # Verify expected options present
    assert "Green" in options
    assert len(options) > 5  # There are multiple color options


@pytest.mark.selenium
def test_select_by_visible_text(driver):
    driver.get("https://demoqa.com/select-menu")

    dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
    dropdown.select_by_visible_text("Blue")

    assert dropdown.first_selected_option.text == "Blue"


@pytest.mark.selenium
def test_multi_select_dropdown(driver):
    driver.get("https://demoqa.com/select-menu")

    # Multi-select dropdown
    multi_dropdown = Select(driver.find_element(By.ID, "cars"))

    # Select multiple options
    multi_dropdown.select_by_visible_text("Volvo")
    multi_dropdown.select_by_visible_text("Saab")

    selected = [opt.text for opt in multi_dropdown.all_selected_options]

    # Validate multiple selections
    assert "Volvo" in selected
    assert "Saab" in selected
    assert len(selected) == 2  # Exactly 2 selected
