import pytest
from pytest_lab.src_lab.pages.inventory_page import InventoryPage


@pytest.mark.selenium
def test_product_listing_count(driver):
    driver.get("https://www.saucedemo.com/")

    # Login first
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    page = InventoryPage(driver)

    products = page.get_all_products()
    assert len(products) == 6, "Product count should be 6"


@pytest.mark.selenium
def test_add_to_cart_and_cart_counter(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    page = InventoryPage(driver)

    # Initially cart should be empty
    assert page.get_cart_count() == 0

    # Add first product
    page.add_first_product_to_cart()

    # Verify cart item count
    assert page.get_cart_count() == 1


@pytest.mark.selenium
def test_price_format_and_validation(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    page = InventoryPage(driver)

    prices = page.get_all_prices()

    # Confirm all prices are > 0
    assert all(p > 0 for p in prices)

    # Verify price list length matches product count
    assert len(prices) == len(page.get_all_products())
