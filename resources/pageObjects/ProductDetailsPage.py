from playwright.sync_api import expect


class ProductDetailsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.get_by_text('Voeg toe')
        self.product_title = page.locator("//h1[@class='typography_typography__OO774 typography_heading-1__"
                                          "onWD2 typography_align-left__gaaF7 product-card-header_title__1W74B']/span")


    def add_product_to_cart(self):
        self.add_to_cart_button.click()

    def validate_product_title(self, product_title_text):
        expect(self.product_title).to_have_text(product_title_text)

    