from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator('//a[@data-testhook="navigation-products"]')
        self.accept_cookie_button = page.locator('#accept-cookies')
        self.decline_cookie_button = page.locator('#decline-cookies')
        self.homepage_title = page.get_by_text('Deze week bij Albert Heijn')

    def click_on_products_navbar(self):
        self.products.click()

    def accept_cookies(self):
        self.accept_cookie_button.click()

    def decline_cookies(self):
        self.decline_cookie_button.click()

    def validate_homepage_is_landed(self):
        expect(self.homepage_title).to_be_visible()
