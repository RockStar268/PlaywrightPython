class FilterProductPage:
    def __init__(self, page):
        self.page = page
        self.body_fit = page.get_by_text('Body & Fit')
        self.show_products_button = page.locator('//button[@class=class="button-or-anchor_root__LgpRR button-default'
                                                 '_root__DAGWZ button-default_primary__mURfJ filters-overlay_'
                                                 'closeButton__8e-Ba"]')

    def click_on_body_fit(self):
        self.body_fit.click()

    def click_show_products_button(self):
        self.show_products_button.click()
