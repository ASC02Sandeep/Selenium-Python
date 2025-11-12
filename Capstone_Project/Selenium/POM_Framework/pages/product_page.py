# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

class ProductPage:
    """Product listing and product detail actions."""

    PRODUCT_TITLES = (By.CSS_SELECTOR, "h2.product-title a")
    ADD_TO_CART_LIST = (By.CSS_SELECTOR, "input.button-2.product-box-add-to-cart-button")
    CART_BADGE = (By.CSS_SELECTOR, "span.cart-qty")
    DETAIL_ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")
    REMOVE_BOXES = (By.NAME, "removefromcart")
    UPDATE_CART_BTN = (By.NAME, "updatecart")
    TOP_CART_LINK = (By.LINK_TEXT, "Shopping cart")

    def __init__(self, driver):
        self.driver = driver

    def titles(self):
        return self.driver.find_elements(*self.PRODUCT_TITLES)

    def cart_count_number(self):
        """Return numeric cart count like (3) → 3"""
        try:
            txt = self.driver.find_element(*self.CART_BADGE).text.strip("()")
            return int(txt)
        except:
            return 0

    def clear_cart_if_any(self):
        """Clear cart fully before test."""
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            qty = badge.text.strip("()")

            if qty and int(qty) > 0:
                badge.click()

                boxes = self.driver.find_elements(*self.REMOVE_BOXES)
                update = self.driver.find_element(*self.UPDATE_CART_BTN)

                for box in boxes:
                    box.click()

                update.click()

        except:
            pass

    def add_from_product_detail(self):
        """Click Add to Cart inside product detail page."""
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DETAIL_ADD_TO_CART)
        )
        btn.click()

    def wait_until_cart_increases(self, old_count):
        """Wait until cart count is old_count+1."""
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.cart_count_number() == old_count + 1
        )

    def prices_float(self):
        """Return all visible product prices as float values."""
        prices = self.driver.find_elements(By.CSS_SELECTOR, "span.price.actual-price")
        numbers = []

        for p in prices:
            txt = p.text.strip().replace("$", "").replace(",", "")
            try:
                numbers.append(float(txt))
            except:
                pass

        return numbers

    def open_cart(self):
        """Open shopping cart page."""
        self.driver.find_element(*self.TOP_CART_LINK).click()

    def remove_all_items(self):
        """Remove all items from cart if present."""
        try:
            remove_boxes = self.driver.find_elements(By.NAME, "removefromcart")
            update_btn = self.driver.find_element(By.NAME, "updatecart")

            for box in remove_boxes:
                box.click()

            update_btn.click()
        except:
            pass

    def safe_get_text(driver, locator, retries=3):
        for _ in range(retries):
            try:
                return driver.find_element(*locator).text
            except StaleElementReferenceException:
                time.sleep(1)
        return ""  # fallback

# # pages/product_page.py
# # Handles product listing, search results, cart operations
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class ProductPage:
#
#     PRODUCT_TITLES = (By.CSS_SELECTOR, "h2.product-title a")
#     ADD_BUTTONS = (By.CSS_SELECTOR, "input[value='Add to cart']")
#     CART_BADGE = (By.CSS_SELECTOR, "span.cart-qty")
#     DETAIL_ADD_BUTTON = (By.CSS_SELECTOR, "input.button-1.add-to-cart-button")
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def titles(self):
#         """Return list of product title elements."""
#         return self.driver.find_elements(*self.PRODUCT_TITLES)
#
#     def cart_count_number(self):
#         """Return cart count as integer."""
#         try:
#             txt = self.driver.find_element(*self.CART_BADGE).text.strip("()")
#             return int(txt) if txt.isdigit() else 0
#         except:
#             return 0
#
#     def add_first_item_to_cart(self):
#         """Click first visible add-to-cart button on search results."""
#         buttons = self.driver.find_elements(*self.ADD_BUTTONS)
#         for b in buttons:
#             if b.is_displayed() and b.is_enabled():
#                 b.click()
#                 return True
#         raise Exception("Add to cart button not found")
#
#     def add_from_product_detail(self):
#         """Click Add-to-cart button inside product details page."""
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(self.DETAIL_ADD_BUTTON)
#         ).click()
#
#     def clear_cart_if_any(self):
#         """If cart has items → go to cart page → remove all items."""
#         try:
#             cart_badge = self.driver.find_element(*self.CART_BADGE)
#             qty = cart_badge.text.strip("()")
#
#             if qty and qty != "0":
#                 cart_badge.click()  # go to cart
#
#                 remove_boxes = self.driver.find_elements(By.NAME, "removefromcart")
#                 update_btn = self.driver.find_element(By.NAME, "updatecart")
#
#                 for box in remove_boxes:
#                     box.click()
#
#                 update_btn.click()
#
#         except:
#             pass
#
#
# # # pages/product_page.py
# # # Covers: list view add, product page add, cart count, price parsing
# #
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# #
# # class ProductPage:
# #     """Product listing and product-detail page utilities."""
# #
# #     # LIST / SEARCH RESULTS PAGE LOCATORS
# #     PRODUCT_TITLES = (By.CSS_SELECTOR, "h2.product-title a")
# #     LIST_ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "input.button-2.product-box-add-to-cart-button")
# #
# #     # PRODUCT-DETAIL PAGE LOCATOR (IMPORTANT!)
# #     DETAIL_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "input.button-1.add-to-cart-button")
# #
# #     # CART BADGE
# #     CART_BADGE = (By.CSS_SELECTOR, "span.cart-qty")   # e.g., "(2)"
# #
# #     def __init__(self, driver):
# #         self.driver = driver
# #
# #     def titles(self):
# #         """Return list of product title elements (used after search)."""
# #         return self.driver.find_elements(*self.PRODUCT_TITLES)
# #
# #     # --------------- LIST VIEW ADD (SEARCH RESULTS) ----------------
# #     def add_from_list_view(self):
# #         """Click first Add-to-Cart button from search results page."""
# #         buttons = self.driver.find_elements(*self.LIST_ADD_TO_CART_BTNS)
# #         if not buttons:
# #             raise Exception("No list view Add-to-Cart buttons found")
# #
# #         for btn in buttons:
# #             if btn.is_displayed() and btn.is_enabled():
# #                 btn.click()
# #                 return True
# #
# #         raise Exception("No clickable Add-to-Cart button in list view")
# #
# #     # --------------- PRODUCT DETAIL PAGE ADD ----------------
# #     def add_from_product_detail(self):
# #         """Click Add-to-Cart button from product detail page."""
# #         btn = WebDriverWait(self.driver, 10).until(
# #             EC.element_to_be_clickable(self.DETAIL_ADD_TO_CART_BTN)
# #         )
# #         btn.click()
# #         return True
# #
# #     # --------------- CART COUNT ----------------
# #     def cart_count_number(self):
# #         """Return numeric cart count from header badge."""
# #         try:
# #             WebDriverWait(self.driver, 5).until(
# #                 EC.visibility_of_element_located(self.CART_BADGE)
# #             )
# #         except:
# #             pass
# #
# #         txt = self.driver.find_element(*self.CART_BADGE).text.strip("()")
# #         return int(txt) if txt.isdigit() else 0
