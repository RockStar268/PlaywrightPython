class ShoppingCart:
    def __init__(self, page):
        self.page = page
        self.shopping_cart_navbar = page.locator("//span[@class='nav-basket_price__FEUe2']")

