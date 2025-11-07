import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# ---------- WEBDRIVER FIXTURE ---------- #
@pytest.fixture(scope="module")
def driver():
    """Setup and teardown for WebDriver"""
    print("\n[Setup] Launching Chrome...")
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    # Login (demo credentials provided by site)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.ENTER)
    time.sleep(2)

    yield driver

    print("\n[Teardown] Closing Chrome...")
    driver.quit()


# ---------- FIXTURES ---------- #
@pytest.fixture
def product_data(driver):
    """Fetch product details dynamically from the page"""
    print("[Fixture] Fetching product details from web...")

    # Get first product name and price
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    # Clean price value (remove $ and convert to float)
    price_value = float(product_price.replace("$", ""))

    return {"name": product_name, "price": price_value}


@pytest.fixture
def product_with_discount(product_data):
    """Apply discount logic"""
    product = product_data.copy()
    product["discount"] = 10  # 10% off
    product["final_price"] = round(product["price"] - (product["price"] * product["discount"] / 100), 2)
    return product


@pytest.fixture
def complete_order(product_with_discount):
    """Complete order fixture depending on product_with_discount"""
    order = {
        "product": product_with_discount,
        "quantity": 2,
        "total_amount": round(product_with_discount["final_price"] * 2, 2),
    }
    return order


# ---------- TESTS ---------- #
def test_product_with_discount(driver, product_with_discount):
    """Validate discount application"""
    print("[Test] Checking discount logic...")
    assert "Sauce" in product_with_discount["name"]
    assert product_with_discount["discount"] == 10
    assert product_with_discount["final_price"] < product_with_discount["price"]

    # Validate the product element is visible
    title_element = driver.find_element(By.CLASS_NAME, "app_logo")
    assert "Swag Labs" in title_element.text


def test_complete_order(driver, complete_order):
    """Validate order total calculation"""
    print("[Test] Checking order total...")
    assert complete_order["quantity"] == 2
    assert complete_order["total_amount"] == round(complete_order["product"]["final_price"] * 2, 2)

    # Example check - verify page URL contains 'inventory'
    assert "inventory" in driver.current_url
