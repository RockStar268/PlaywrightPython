from ...resources.pageObjects.ProductPage import ProductPage
from ...resources.pageObjects.Navbar import Navbar
from ...resources.pageObjects.ProductFilterSidebar import ProductFilterSideBar
from ...resources.pageObjects.ProductDetailsPage import ProductDetailsPage
from ...resources.pageObjects.ShoppingCart import ShoppingCart
from playwright.sync_api import expect

import pytest


# @pytest.mark.skip_browser("chromium")  # for skipping declared browser annotation
# @pytest.mark.only_browser("firefox")  # for running only in 1 type of browser annotation
@pytest.mark.smoke
@pytest.mark.parametrize("category, brand , product_name", [
    ("Frisdrank, sappen, koffie, thee", "Starbucks", "Starbucks Single-origin Colombia koffiebonen")])
def test_select_category_navbar(set_up, category, brand, product_name):
    page = set_up
    navbar = Navbar(page)
    product_page = ProductPage(page)
    product_filter_sidebar = ProductFilterSideBar(page)
    product_details = ProductDetailsPage(page)
    shopping_cart = ShoppingCart(page)

    navbar.click_on_products()
    product_page.click_on_category(category)

    # filtering sidebar on product page
    product_filter_sidebar.click_on_brand(brand)

    # select product and add to cart
    product_page.select_product(product_name)
    product_details.validate_product_title(product_name)
    product_details.add_product_to_cart()

    # validate product is added to shopping cart
    expect(shopping_cart.shopping_cart_navbar).not_to_have_text("0.00")
