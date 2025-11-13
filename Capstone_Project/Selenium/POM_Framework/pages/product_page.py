# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    """Handles product list and cart operations."""

    PRODUCT_TITLES = (By.CSS_SELECTOR, "h2.product-title a")
    DETAIL_ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")
    TOP_CART_LINK = (By.LINK_TEXT, "Shopping cart")
    REMOVE_BOXES = (By.NAME, "removefromcart")
    UPDATE_CART_BTN = (By.NAME, "updatecart")
    CART_BADGE = (By.CSS_SELECTOR, "span.cart-qty")

    def __init__(self, driver):
        self.driver = driver

    def titles(self):
        """Return list of visible product titles."""
        return self.driver.find_elements(*self.PRODUCT_TITLES)

    def add_from_product_detail(self):
        """Click Add to Cart button from product detail page."""
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DETAIL_ADD_TO_CART)
        )
        btn.click()

    def open_cart(self):
        """Open shopping cart page."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TOP_CART_LINK)
        ).click()

    def remove_all_items(self):
        """Remove all items from the shopping cart if present."""
        try:
            checkboxes = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.REMOVE_BOXES)
            )
            for box in checkboxes:
                box.click()

            update = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.UPDATE_CART_BTN)
            )
            update.click()
        except:
            pass

    def cart_count_number(self):
        """Return numeric cart count safely."""
        try:
            qty_text = self.driver.find_element(*self.CART_BADGE).text.strip("()")
            return int(qty_text) if qty_text else 0
        except:
            return 0

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




