class SportDietProductPage:
    def __init__(self, page):
        self.page = page
        self.relevance_dropdown = page.locator('//select[@data-testhook="sorting"]')
        # self.relevance_dropdown_nutriscore = page.locator('//select[@data-testhook="sorting"]').select_option(
        #     value="?sortBy=nutriscore")
        self.filter_dropdown = page.get_by_text('Filter')

    def select_relevance_dropdown_nutriscore(self):
        self.relevance_dropdown.select_option(value="?sortBy=nutriscore")

    def click_on_filter(self):
        self.filter_dropdown.click()

