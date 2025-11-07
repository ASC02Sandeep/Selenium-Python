import pytest
from Nov_6.src_lab.pages.login_page import LoginPage
from Nov_6.src_lab.pages.inventory_page import InventoryPage

@pytest.mark.cart
@pytest.mark.regression
def test_add_to_cart(driver):
    login = LoginPage(driver)
    inv = InventoryPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")
    inv.add_item()

    assert inv.get_cart_count() == "1"
