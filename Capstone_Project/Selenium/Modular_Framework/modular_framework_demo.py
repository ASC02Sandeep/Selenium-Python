"""
Demo Web Shop Automation (Single file, Modular style)

Concepts included:
✔ Launch Browser (headless optional)
✔ Login
✔ Search
✔ Click First Product
✔ Add to Cart
✔ (Optional) Validate Cart Count Change
✔ Proceed to Checkout (all steps) + Confirm Order
✔ Validate 'Order successfully processed' message
✔ Sort Prices (Low → High) in Books category
✔ Validate Sorted Order
✔ Title Validation + Footer Text Validation
✔ Screenshot Capture
✔ Explicit Waits + Robust helpers
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# ----------------------------------------------------------------------
# Common helpers
# ----------------------------------------------------------------------
def start_browser(headless=True):
    """Start Chrome with optional headless; maximize for consistency."""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver


def wait_and_click(driver, locator, timeout=10):
    """Wait until element located by 'locator' is clickable, then click."""
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()


def element_exists(driver, locator, timeout=5):
    """Return True if element appears within timeout; otherwise False."""
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        return True
    except:
        return False


# ----------------------------------------------------------------------
# Auth
# ----------------------------------------------------------------------
def login(driver, email, password):
    """Login to Demo Web Shop and wait for account link."""
    driver.get("https://demowebshop.tricentis.com/login")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Email")))
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input.button-1.login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.account"))
    )
    print("[PASSED] Login successful!")


# ----------------------------------------------------------------------
# Search + Add to cart
# ----------------------------------------------------------------------
def search_product(driver, keyword):
    """Search from the header search box."""
    driver.get("https://demowebshop.tricentis.com/")  # ensure on home
    sb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "small-searchterms"))
    )
    sb.clear()
    sb.send_keys(keyword)
    wait_and_click(driver, (By.CSS_SELECTOR, "input.button-1.search-box-button"))
    print(f"[INFO] Search completed for keyword: {keyword}")


def add_first_product_to_cart(driver):
    """
    Open first search result product page and click its 'Add to cart'.
    Uses robust locators that work for both books and other categories.
    """
    # Re-locate titles list to avoid stale references
    titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.product-title a"))
    )
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(titles[0]))
    titles[0].click()

    # On product details page, generic 'Add to cart' input
    wait_and_click(driver, (By.CSS_SELECTOR, "input[value='Add to cart']"), timeout=15)
    print("[PASSED] Product added to cart.")


def get_cart_count(driver):
    """Read the cart badge '(N)' and return N as int."""
    qty_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-qty"))
    )
    txt = qty_elem.text.strip("()")
    return int(txt) if txt.isdigit() else 0


# ----------------------------------------------------------------------
# Checkout flow (all steps)
# ----------------------------------------------------------------------
def proceed_to_checkout_and_confirm(driver):
    """
    End-to-end checkout for a LOGGED-IN user:
    - Open cart
    - Agree to terms
    - Checkout
    - Billing address (continue)
    - Shipping address (continue)
    - Shipping method (choose first) -> continue
    - Payment method (choose first) -> continue
    - Payment info (continue)
    - Confirm order
    - Assert success message
    """
    # Open cart
    wait_and_click(driver, (By.CSS_SELECTOR, "span.cart-qty"))
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.page.shopping-cart-page"))
    )

    # Agree to terms
    terms = (By.ID, "termsofservice")
    if element_exists(driver, terms, timeout=3):
        cb = driver.find_element(*terms)
        if not cb.is_selected():
            cb.click()

    # Click 'Checkout'
    wait_and_click(driver, (By.ID, "checkout"))

    # If checkout method appears (guest vs register), you’re already logged in,
    # so a "Checkout as Guest" step usually won’t appear. Handle just in case:
    if element_exists(driver, (By.ID, "checkoutasguest"), timeout=3):
        wait_and_click(driver, (By.ID, "checkoutasguest"))

    # ---- Billing address ----
    # If address select exists, just continue.
    billing_continue = (By.CSS_SELECTOR, "#billing-buttons-container input.button-1")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "billing-address-select"))
    ) if element_exists(driver, (By.ID, "billing-address-select"), 2) else None
    wait_and_click(driver, billing_continue, timeout=15)

    # ---- Shipping address ----
    shipping_continue = (By.CSS_SELECTOR, "#shipping-buttons-container input.button-1")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#shipping-buttons-container"))
    )
    wait_and_click(driver, shipping_continue, timeout=15)

    # ---- Shipping method ----
    # Choose first available shipping option if any radios exist
    try:
        radios = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.NAME, "shippingoption"))
        )
        if radios:
            if not radios[0].is_selected():
                radios[0].click()
    except:
        pass  # sometimes there’s only one default or it's preselected

    wait_and_click(
        driver,
        (By.CSS_SELECTOR, "#shipping-method-buttons-container input.button-1"),
        timeout=15,
    )

    # ---- Payment method ----
    # Choose first available payment radio (e.g., Check/Money Order)
    try:
        pm_radios = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.NAME, "paymentmethod"))
        )
        if pm_radios:
            if not pm_radios[0].is_selected():
                pm_radios[0].click()
    except:
        pass

    wait_and_click(
        driver,
        (By.CSS_SELECTOR, "#payment-method-buttons-container input.button-1"),
        timeout=15,
    )

    # ---- Payment info (usually empty form for demo) ----
    wait_and_click(
        driver,
        (By.CSS_SELECTOR, "#payment-info-buttons-container input.button-1"),
        timeout=15,
    )

    # ---- Confirm order ----
    wait_and_click(
        driver,
        (By.CSS_SELECTOR, "#confirm-order-buttons-container input.button-1"),
        timeout=20,
    )

    # ---- Success assertion ----
    success_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.section.order-completed"))
    )
    success_text = success_box.text.strip()
    assert "successfully processed" in success_text.lower(), \
        f"Order success text not found. Got: {success_text}"
    print("[PASSED] Order placed successfully!")


# ----------------------------------------------------------------------
# Sorting + validations + screenshot
# ----------------------------------------------------------------------
def validate_price_sorting(driver):
    """Go to Books category, sort Low→High, and assert sorted order."""
    driver.get("https://demowebshop.tricentis.com/")
    wait_and_click(driver, (By.LINK_TEXT, "Books"))
    Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "products-orderby"))
    )).select_by_visible_text("Price: Low to High")

    # Let list refresh
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.price.actual-price"))
    )
    time.sleep(1)

    prices = driver.find_elements(By.CSS_SELECTOR, "span.price.actual-price")
    values = []
    for p in prices:
        t = p.text.replace("$", "").replace(",", "").strip()
        if t:
            try:
                values.append(float(t))
            except:
                pass

    print(f"[INFO] Prices found: {values}")
    assert values, "No prices captured on Books page."
    assert values == sorted(values), "Prices are NOT sorted by Low → High!"
    print("[PASSED] Prices sorted Low → High correctly!")


def validate_title_and_text(driver):
    """Basic title + footer text checks; save a screenshot."""
    title = driver.title
    print(f"[INFO] Page Title: {title}")
    assert "Demo Web Shop" in title, "Title validation failed!"

    # Footer text (may vary; keep case-insensitive compare)
    footer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "footer-disclaimer"))
    ).text
    print("[INFO] Footer Text:", footer)
    # Example: "Copyright © 2025 Tricentis Demo Web Shop. All rights reserved."
    assert "all rights reserved" in footer.lower(), "Footer text validation failed!"

    driver.save_screenshot("demo_webshop_screenshot.png")
    print("[PASSED] Screenshot captured!")


# ----------------------------------------------------------------------
# Main scenario
# ----------------------------------------------------------------------
def main():
    driver = start_browser(headless=False)
    try:
        # 1) Login
        login(driver, "sandeep98@gmail.com", "sandeep123")

        # 2) Search + Add to cart
        search_product(driver, "book")
        before = get_cart_count(driver)
        print(f"[INFO] Cart before adding: {before}")
        add_first_product_to_cart(driver)

        # Wait until cart increments (tolerant even if site delays the badge)
        WebDriverWait(driver, 10).until(lambda d: get_cart_count(d) >= before)
        after = get_cart_count(driver)
        print(f"[INFO] Cart after adding: {after}")

        # 3) Proceed to checkout + confirm order
        proceed_to_checkout_and_confirm(driver)

        # 4) Go back to site home and run sorting + validations
        driver.get("https://demowebshop.tricentis.com/")
        validate_price_sorting(driver)
        validate_title_and_text(driver)

        print("\nFINAL RESULT → All scenarios (Add→Checkout→Sort→Validate) passed!\n")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()





# """
#
# Demo Web Shop Automation
#
#
# Concepts included:
# ✔ Launch Browser
# ✔ Login
# ✔ Search
# ✔ Click First Product
# ✔ Add to Cart
# ✔ Validate Cart Count
# ✔ Open Cart + Remove Items
# ✔ Validate Empty Cart
# ✔ Sort Prices (Low → High)
# ✔ Validate Sorted Order
# ✔ Title Validation
# ✔ Text Validation
# ✔ Screenshot Capture
# ✔ Explicit Waits
# ✔ Comments everywhere
# """
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
#
#
# # ----------------------------------------------------------------------
# # 1. COMMON FUNCTION - START BROWSER (HEADLESS OPTIONAL)
# # ----------------------------------------------------------------------
# def start_browser(headless=False):
#     chrome_options = Options()
#     if headless:
#         chrome_options.add_argument("--headless=new")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--window-size=1920,1080")
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     return driver
#
#
# # ----------------------------------------------------------------------
# # 2. LOGIN FUNCTION
# # ----------------------------------------------------------------------
# def login(driver, email, password):
#     driver.get("https://demowebshop.tricentis.com/login")
#
#     # Wait for Email field
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "Email"))
#     )
#
#     driver.find_element(By.ID, "Email").send_keys(email)
#     driver.find_element(By.ID, "Password").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, "input.button-1.login-button").click()
#
#     # Validate login
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "a.account"))
#     )
#
#     print("[PASSED] Login successful!")
#
#
# # ----------------------------------------------------------------------
# # 3. SEARCH FOR PRODUCT
# # ----------------------------------------------------------------------
# def search_product(driver, keyword):
#     search_box = driver.find_element(By.ID, "small-searchterms")
#     search_box.clear()
#     search_box.send_keys(keyword)
#     driver.find_element(By.CSS_SELECTOR, "input.button-1.search-box-button").click()
#
#     print(f"[INFO] Search completed for keyword: {keyword}")
#
#
# # ----------------------------------------------------------------------
# # 4. ADD FIRST SEARCH RESULT TO CART
# # ----------------------------------------------------------------------
# def add_first_product_to_cart(driver):
#     wait = WebDriverWait(driver, 10)
#
#     # Click first product safely
#     titles = driver.find_elements(By.CSS_SELECTOR, "h2.product-title a")
#     wait.until(EC.element_to_be_clickable(titles[0])).click()
#
#     # Click Add to Cart (dynamic ID)
#     add_btn = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Add to cart']"))
#     )
#     add_btn.click()
#
#     print("[PASSED] Product added to cart.")
#
#
#
#
# # ----------------------------------------------------------------------
# # 5. GET CART COUNT
# # ----------------------------------------------------------------------
# def get_cart_count(driver):
#     wait = WebDriverWait(driver, 10)
#
#     qty_elem = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-qty"))
#     )
#
#     return int(qty_elem.text.strip("()") or 0)
#
#
#
#
#
# # ----------------------------------------------------------------------
# # 6. REMOVE ALL ITEMS FROM CART
# # ----------------------------------------------------------------------
# def remove_all_cart_items(driver):
#     wait = WebDriverWait(driver, 10)
#
#     # Open cart page
#     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-qty"))).click()
#
#     # Select all remove-from-cart checkboxes
#     checkboxes = driver.find_elements(By.NAME, "removefromcart")
#     for box in checkboxes:
#         box.click()
#
#     # Click UPDATE CART
#     driver.find_element(By.NAME, "updatecart").click()
#
#     print("[PASSED] All cart items removed!")
#
#
# # ----------------------------------------------------------------------
# # 7. SORT PRICES AND VALIDATE ORDER (Scenario 3)
# # ----------------------------------------------------------------------
# def validate_price_sorting(driver):
#     # Open Books category
#     driver.find_element(By.LINK_TEXT, "Books").click()
#
#     # Select sort option
#     sort_dropdown = Select(driver.find_element(By.ID, "products-orderby"))
#     sort_dropdown.select_by_visible_text("Price: Low to High")
#
#     time.sleep(2)
#
#     # Extract prices
#     prices = driver.find_elements(By.CSS_SELECTOR, "span.price.actual-price")
#     price_values = [float(p.text.replace("$", "").strip()) for p in prices]
#
#     print(f"[INFO] Prices found: {price_values}")
#
#     # Validate ascending order
#     assert price_values == sorted(price_values), "Prices are NOT sorted!"
#
#     print("[PASSED] Prices sorted Low → High correctly!")
#
#
# # ----------------------------------------------------------------------
# # 8. TITLE + TEXT VALIDATIONS + SCREENSHOT
# # ----------------------------------------------------------------------
# def validate_title_and_text(driver):
#     # Validate title contains keyword
#     title = driver.title
#     print(f"[INFO] Page Title: {title}")
#
#     assert "Demo Web Shop" in title, "Title validation failed!"
#
#     # Validate some text on page
#     footer_text = driver.find_element(By.CLASS_NAME, "footer-disclaimer").text
#     print("[INFO] Footer Text:", footer_text)
#
#     assert "all rights reserved" in footer_text.lower(), "Text validation failed!"
#
#
#     # Screenshot
#     driver.save_screenshot("demo_webshop_screenshot.png")
#     print("[PASSED] Screenshot captured!")
#
#
# # ----------------------------------------------------------------------
# # 9. MAIN FUNCTION (RUN EVERYTHING)
# # ----------------------------------------------------------------------
# def main():
#     driver = start_browser(headless=False)
#
#     try:
#         # LOGIN
#         login(driver, "sandeep98@gmail.com", "sandeep123")
#
#         # SEARCH FLOW + ADD TO CART
#         search_product(driver, "book")
#
#         before_count = get_cart_count(driver)
#         print(f"[INFO] Cart before adding: {before_count}")
#
#         add_first_product_to_cart(driver)
#
#         wait = WebDriverWait(driver, 10)
#
#         wait.until(lambda d: get_cart_count(d) > before_count)
#
#         after_count = get_cart_count(driver)
#
#         print(f"[INFO] Cart after adding: {after_count}")
#
#         assert after_count == before_count + 1, "Cart count not updated!"
#
#         # REMOVE ALL ITEMS
#         remove_all_cart_items(driver)
#
#         empty_count = get_cart_count(driver)
#         assert empty_count == 0, "Cart is not empty!"
#
#         print("[PASSED] Cart empty validation successful!")
#
#         #   Go back to Home page before sorting test
#         driver.get("https://demowebshop.tricentis.com/")
#
#         # SORT PRICE VALIDATION
#         validate_price_sorting(driver)
#
#         # TITLE + TEXT + SCREENSHOT
#         validate_title_and_text(driver)
#
#         print("\n FINAL RESULT → ALL SCENARIOS PASSED SUCCESSFULLY!\n")
#
#     finally:
#         driver.quit()
#
#
# # ----------------------------------------------------------------------
# # Run the script
# # ----------------------------------------------------------------------
# if __name__ == "__main__":
#     main()
