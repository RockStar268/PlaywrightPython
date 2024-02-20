class HomePage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator('//a[@data-testhook="navigation-products"]')
        self.accept_cookie_button = page.locator('#accept-cookies')
        self.decline_cookie_button = page.locator('#decline-cookies')
        self.cookies_popup = page.get_by_role("heading", name="Cookies op ah.nl")


    def click_on_products_navbar(self):
        self.products.click()

    def accept_cookies(self):
        self.accept_cookie_button.click()

    def decline_cookies(self):
        self.decline_cookie_button.click()



