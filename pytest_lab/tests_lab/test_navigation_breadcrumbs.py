import pytest
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_navigation_and_title(driver):
    driver.get("https://demowebshop.tricentis.com/")

    # Click "Books" category
    driver.find_element(By.LINK_TEXT, "Books").click()

    # Verify page title changed
    assert "Books" in driver.title

    # Verify URL changed
    assert "books" in driver.current_url.lower()


@pytest.mark.selenium
def test_back_and_forward_navigation(driver):
    driver.get("https://demowebshop.tricentis.com/")

    # Go to Electronics page
    driver.find_element(By.LINK_TEXT, "Electronics").click()
    electronics_url = driver.current_url

    # Go back
    driver.back()
    assert "demowebshop" in driver.current_url.lower()

    # Go forward
    driver.forward()
    assert driver.current_url == electronics_url


@pytest.mark.selenium
def test_breadcrumb_trail(driver):
    driver.get("https://demowebshop.tricentis.com/")

    # Navigate to apparel
    driver.find_element(By.LINK_TEXT, "Apparel & Shoes").click()

    # Click a product
    driver.find_element(By.LINK_TEXT, "Blue Jeans").click()

    # Verify breadcrumb trail
    breadcrumb = driver.find_element(By.CSS_SELECTOR, "div.breadcrumb")
    breadcrumb_text = breadcrumb.text

    assert "Home" in breadcrumb_text
    assert "Apparel & Shoes" in breadcrumb_text
    assert "Blue Jeans" in breadcrumb_text
