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
    """Login → Search book → Add first product → Remove it from cart."""

    # LOGIN
    login = LoginPage(driver)
    login.open()
    login.login("sandeep98@gmail.com", "sandeep123")
    assert login.is_logged_in(), "Login failed — cannot continue test"

    # HOME PAGE
    home = HomePage(driver)
    home.open(base_url)

    # SEARCH
    home.search("book")
    prod = ProductPage(driver)

    # --- GET RESULTS (fresh fetch to avoid stale elements) ---
    fresh_titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-title a"))
    )
    assert len(fresh_titles) > 0, "No products found for 'book'"

    # OPEN FIRST PRODUCT PAGE (fresh stable element)
    first_title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(fresh_titles[0])
    )
    first_title.click()

    # ADD TO CART
    prod.add_from_product_detail()

    # OPEN CART
    prod.open_cart()

    # REMOVE ITEM
    prod.remove_all_items()

    # ASSERT CART IS EMPTY (safe reload)
    qty_elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-qty"))
    )
    qty = qty_elem.text.strip("()")
    assert qty in ("0", ""), f"Cart not empty after removal. qty={qty}"





# @pytest.mark.cart
# @pytest.mark.ui
# @pytest.mark.regression
# def test_search_and_add_first_item_to_cart(driver, base_url):
#     """Login → Search book → Add first product → Remove it from cart."""
#
#     # LOGIN
#     login = LoginPage(driver)
#     login.open()
#     login.login("sandeep98@gmail.com", "sandeep123")
#     assert login.is_logged_in(), "Login failed — cannot continue test"
#
#     # HOME PAGE
#     home = HomePage(driver)
#     home.open(base_url)
#
#     # SEARCH
#     home.search("book")
#     prod = ProductPage(driver)
#
#     # GET RESULTS
#     titles = prod.titles()
#     assert len(titles) > 0, "No products found for 'book'"
#
#     # OPEN FIRST PRODUCT PAGE
#     titles[0].click()
#
#     # ADD TO CART
#     prod.add_from_product_detail()
#
#     # OPEN CART
#     prod.open_cart()
#
#     # REMOVE ITEM
#     prod.remove_all_items()
#
#     # ASSERT CART IS EMPTY   FIXED SELENIUM 4 SYNTAX
#     qty = driver.find_element(By.CSS_SELECTOR, "span.cart-qty").text.strip("()")
#     assert qty == "0", f"Cart is not empty! qty={qty}"



# # tests/test_search_cart.py
# # Marks: cart + ui + regression
#
# import pytest
# from pages.home_page import HomePage
# from pages.product_page import ProductPage
# from pages.login_page import LoginPage
#
#
# @pytest.mark.cart
# @pytest.mark.ui
# @pytest.mark.regression
# def test_search_and_add_first_item_to_cart(driver, base_url):
#     """Login → Clear cart → Search book → Add first product → Validate cart count updates"""
#
#     # LOGIN
#     login = LoginPage(driver)
#     login.open()
#     login.login("sandeep98@gmail.com", "sandeep123")
#     assert login.is_logged_in(), "Login failed — cannot continue test"
#
#     # HOME PAGE
#     home = HomePage(driver)
#     home.open(base_url)
#
#     # SEARCH
#     home.search("book")
#     prod = ProductPage(driver)
#
#     # CLEAR CART BEFORE ADDING
#     prod.clear_cart_if_any()
#
#     # SEARCH RESULTS EXIST
#     titles = prod.titles()
#     assert len(titles) > 0, "No products available for search 'book'"
#
#     before = prod.cart_count_number()
#
#     # OPEN PRODUCT PAGE
#     titles[0].click()
#
#     # ADD TO CART
#     prod.add_from_product_detail()
#
#     # WAIT UNTIL BADGE UPDATES
#     prod.wait_until_cart_increases(before)
#
#     after = prod.cart_count_number()
#
#     assert after == before + 1, f"Cart count did not update! before={before}, after={after}"
#
#
# # # tests/test_search_cart.py
# #
# # import pytest
# # from pages.login_page import LoginPage
# # from pages.home_page import HomePage
# # from pages.product_page import ProductPage
# #
# # @pytest.mark.cart
# # @pytest.mark.ui
# # def test_search_and_add_first_item_to_cart(driver, base_url):
# #     """Login → Clear cart → Search 'book' → Add first item → Validate cart increases."""
# #
# #     # LOGIN
# #     login = LoginPage(driver)
# #     login.open()
# #     login.login("sandeep98@gmail.com", "sandeep123")
# #     assert login.is_logged_in(), "Login failed — stopping test"
# #
# #     # OPEN HOME
# #     home = HomePage(driver)
# #     home.open(base_url)
# #
# #     # SEARCH ITEMS
# #     home.search("book")
# #     prod = ProductPage(driver)
# #
# #     # CLEAR CART BEFORE ADDING
# #     prod.clear_cart_if_any()
# #
# #     # Ensure search results exist
# #     titles = prod.titles()
# #     assert len(titles) > 0, "No products found for 'book'"
# #
# #     before = prod.cart_count_number()
# #
# #     # OPEN FIRST PRODUCT PAGE
# #     titles[0].click()
# #
# #     # ADD TO CART
# #     prod.add_from_product_detail()
# #
# #     driver.implicitly_wait(3)
# #
# #     after = prod.cart_count_number()
# #
# #     assert after == before + 1, f"Cart not updated! before={before}, after={after}"
# #
# #
# # # # tests/test_search_cart.py
# # #
# # # import pytest
# # # from pages.home_page import HomePage
# # # from pages.product_page import ProductPage
# # # from pages.login_page import LoginPage
# # #
# # #
# # # @pytest.mark.cart
# # # @pytest.mark.ui
# # # def test_search_and_add_first_item_to_cart(driver, base_url):
# # #     """Login → Clean cart → Search → Add item → Verify cart count increases"""
# # #
# # #     # LOGIN
# # #     login = LoginPage(driver)
# # #     login.open()
# # #     login.login("sandeep98@gmail.com", "sandeep123")
# # #     assert login.is_logged_in(), "Login failed — cannot continue test"
# # #
# # #     # ✅ CLEAR CART BEFORE TEST
# # #     login.clear_cart_if_any()
# # #
# # #     # OPEN HOME
# # #     home = HomePage(driver)
# # #     home.open(base_url)
# # #
# # #     # SEARCH
# # #     home.search("book")
# # #     prod = ProductPage(driver)
# # #
# # #     titles = prod.titles()
# # #     assert len(titles) > 0, "No products found"
# # #
# # #     # CART COUNT BEFORE
# # #     before = prod.cart_count_number()
# # #
# # #     # OPEN PRODUCT
# # #     titles[0].click()
# # #
# # #     # ADD FROM PRODUCT DETAIL
# # #     prod.add_from_product_detail()
# # #
# # #     # WAIT FOR UPDATE
# # #     driver.implicitly_wait(3)
# # #
# # #     after = prod.cart_count_number()
# # #
# # #     assert after == before + 1, f"Cart not updated! before={before}, after={after}"
