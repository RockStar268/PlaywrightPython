class ProductFilterSideBar:
    def __init__(self, page):
        self.page = page
        self.show_more = page.get_by_text("Toon meer")

    def select_nutriscore(self, nutriscore):
        nutriscore = self.page.locator(f"//span[@class='checkbox_box__5e-tj checkbox_box__G+6Ge']/../..//span[text()='{nutriscore}']")

        if nutriscore.is_hidden():
            self.show_more.nth(0).click()
            if not nutriscore.is_hidden():
                 nutriscore.click()
        else:
            nutriscore.click()

    def click_on_brand(self, brand):
        get_brand = self.page.locator(f"//span[text()='{brand}']")
        if get_brand.is_hidden():
            self.show_more.nth(1).click()
            get_brand.click()
        else:
            get_brand.click()


