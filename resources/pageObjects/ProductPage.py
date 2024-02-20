class ProductPage:
    def __init__(self, page):
        self.page = page
        self.show_more_results_button = page.locator("//button[@data-testhook='load-more']")

    def click_on_category(self, category):
        self.page.get_by_role("link", name=category).first.click()

    def show_more_results(self):
        self.show_more_results_button.click()

    def select_product(self, product):
        get_product = self.page.locator(f"//span[text()='{product}']")

        if get_product.is_hidden():
            ProductPage.show_more_results(self)
            get_product.click()
        else:
            get_product.click()
