import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.selenium
def test_element_becomes_visible(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    # Wait for the button that becomes visible after 5 seconds
    visible_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    assert visible_button.is_displayed()


@pytest.mark.selenium
def test_progress_bar_update(driver):
    driver.get("https://demoqa.com/progress-bar")

    start_button = driver.find_element(By.ID, "startStopButton")
    progress_label = driver.find_element(By.CSS_SELECTOR, "div[role='progressbar']")

    start_button.click()

    # Wait until progress reaches at least 80%
    WebDriverWait(driver, 15).until(
        lambda d: int(progress_label.get_attribute("aria-valuenow")) >= 80
    )

    value = int(progress_label.get_attribute("aria-valuenow"))
    assert value >= 80


@pytest.mark.selenium
def test_infinite_scroll(driver):
    driver.get("https://demoqa.com/infinite-scroll")

    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(3):  # Scroll 3 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(2)

    new_height = driver.execute_script("return document.body.scrollHeight")

    assert new_height > last_height


@pytest.mark.selenium
def test_real_time_auto_complete_search(driver):
    driver.get("https://demoqa.com/auto-complete")

    input_box = driver.find_element(By.ID, "autoCompleteMultipleInput")
    input_box.send_keys("re")  # Trigger suggestions

    results = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.auto-complete__option"))
    )

    assert any("re" in r.text.lower() for r in results)
