from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    product_cards = (By.CLASS_NAME, "inventory_item")
    add_to_cart_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    product_prices = (By.CLASS_NAME, "inventory_item_price")

    def get_all_products(self):
        return self.driver.find_elements(*self.product_cards)

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0  # No items added yet

    def get_all_prices(self):
        elements = self.driver.find_elements(*self.product_prices)
        return [float(e.text.replace("$", "")) for e in elements]
