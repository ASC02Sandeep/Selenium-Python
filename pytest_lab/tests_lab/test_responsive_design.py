import pytest
from selenium.webdriver.common.by import By

# Helper Login Function
def login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


@pytest.mark.selenium
def test_desktop_view_elements(driver):
    driver.set_window_size(1366, 768)  # Desktop resolution
    login(driver)

    # Desktop: 'Products' Title should be visible
    title = driver.find_element(By.CLASS_NAME, "title")
    assert title.is_displayed() and title.text == "Products"


@pytest.mark.selenium
def test_mobile_hamburger_menu(driver):
    driver.set_window_size(375, 812)  # iPhone size
    login(driver)

    # Check hamburger menu is visible on smaller screens
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_button.is_displayed()

    # Open menu
    menu_button.click()

    # Check logout is visible inside side menu
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    assert logout_link.is_displayed()


@pytest.mark.selenium
def test_layout_change_on_resize(driver):
    login(driver)

    # Get product elements count in desktop
    driver.set_window_size(1366, 768)
    desktop_products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    desktop_count = len(desktop_products)

    # Switch to mobile size
    driver.set_window_size(375, 812)
    mobile_products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    mobile_count = len(mobile_products)

    # Product count remains the same, but layout changes
    assert desktop_count == mobile_count


@pytest.mark.selenium
def test_cart_visibility_mobile_vs_desktop(driver):
    login(driver)

    # Desktop
    driver.set_window_size(1600, 900)
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert cart_icon.is_displayed()

    # Mobile view
    driver.set_window_size(375, 812)
    cart_icon_mobile = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert cart_icon_mobile.is_displayed()
