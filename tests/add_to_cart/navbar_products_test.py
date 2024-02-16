from ...resources.pageObjects.HomePage import HomePage
from ...resources.pageObjects.ProductPage import ProductPage
from ...resources.pageObjects.SportDietProductPage import SportDietProductPage
from ...resources.pageObjects.FilterProductPage import FilterProductPage
import pytest


# @pytest.mark.skip_browser("chromium")  # for skipping declared browser annotation
# @pytest.mark.only_browser("firefox")  # for running only in 1 type of browser annotation
@pytest.mark.smoke
def test_select_product_navbar_sport(set_up):
    page = set_up
    homepage = HomePage(page)
    productpage = ProductPage(page)
    sportdietpage = SportDietProductPage(page)
    filterproductpage = FilterProductPage(page)

    homepage.validate_homepage_is_landed()

    if homepage.accept_cookie_button.is_visible():
        homepage.accept_cookies()

    homepage.click_on_products_navbar()
    productpage.click_on_sport_dieet_category()

    # filter based on nutriscore
    sportdietpage.select_relevance_dropdown_nutriscore()

    # select body and fit from filter dropdown
    sportdietpage.click_on_filter()
    filterproductpage.click_on_body_fit()
    filterproductpage.click_show_products_button()
