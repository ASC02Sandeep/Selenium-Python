# tests/test_sort_and_prices.py
# Marks: regression + ui; dropdown + price parsing

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.ui
@pytest.mark.regression
def test_sort_low_to_high_and_validate_prices(driver, base_url):
    """Open Books -> sort by 'Price: Low to High' -> verify sorted order."""
    home = HomePage(driver)
    home.open(base_url)
    home.go_to_books()

    # Classic <select> dropdown on category list
    order = Select(driver.find_element(By.ID, "products-orderby"))
    order.select_by_visible_text("Price: Low to High")

    prod = ProductPage(driver)
    prices = prod.prices_float()
    assert len(prices) > 0
    assert prices == sorted(prices)
