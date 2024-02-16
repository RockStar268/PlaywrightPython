class ProductPage:
    def __init__(self, page):
        self.page = page
        self.sport_diet_category = page.locator('//div[@class="taxonomy-card_title__vBWel"]//a[@title="Sport- en dieetvoeding"]')
        self.bakery_category = page.get_by_text('Bakkerij en banket')

    def click_on_sport_dieet_category(self):
        self.sport_diet_category.click()


    def click_on_bakery_category(self):
        self.bakery_category.click()

