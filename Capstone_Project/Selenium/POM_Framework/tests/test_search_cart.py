# tests/test_search_cart.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


@pytest.mark.cart
@pytest.mark.ui
@pytest.mark.regression
def test_search_and_add_first_item_to_cart(driver, base_url):
    """
    Test Scenario:
     Login
     Search for 'book'
    Open first product
     Add to cart
     Open cart and remove all items
     Validate cart is empty
    """

    # --- LOGIN ---
    login = LoginPage(driver)
    login.open()
    login.login("sandeep98@gmail.com", "sandeep123")
    assert login.is_logged_in(), "Login failed — cannot continue test"

    # --- HOME PAGE ---
    home = HomePage(driver)
    home.open(base_url)

    # --- SEARCH ---
    home.search("book")
    prod = ProductPage(driver)

    # --- GET RESULTS (fresh fetch to avoid stale elements) ---
    fresh_titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-title a"))
    )
    assert len(fresh_titles) > 0, "No products found for 'book'"

    # --- OPEN FIRST PRODUCT PAGE (refetch to avoid stale element reference) ---
    first_product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-title a"))
    )
    first_product_link.click()

    # --- ADD TO CART ---
    prod.add_from_product_detail()

    # --- OPEN CART ---
    prod.open_cart()

    # --- REMOVE ALL ITEMS FROM CART ---
    prod.remove_all_items()

    # --- ASSERT CART IS EMPTY ---
    qty_elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-qty"))
    )
    qty = qty_elem.text.strip("()")
    assert qty in ("0", ""), f"❌ Cart not empty after removal. Found qty={qty}"

    print("✅ [PASSED] Cart successfully emptied after adding and removing an item.")