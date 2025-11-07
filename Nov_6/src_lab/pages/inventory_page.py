from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_count = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item(self):
        self.driver.find_element(*self.add_backpack).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text
