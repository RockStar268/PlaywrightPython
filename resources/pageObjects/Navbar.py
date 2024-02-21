class Navbar:
    def __init__(self, page):
        self.page = page
        self.products = page.locator('//a[@data-testhook="navigation-products"]')
        self.account = page.locator('//div[@class="user-icon_container__5+nqK icon-button_icon__qsWNH"]')

    def click_on_products(self):
        self.products.click()

    def click_on_my_account(self):
        self.account.click()


