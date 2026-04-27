class FarmersPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        # Navigate via click, not direct URL — session must already be active
        self.page.click('//*[@id="module-secondary-operational"]/nav/div[1]/div/button')
        self.page.click('//*[@id="module-secondary-operational"]/nav/div[1]/div[2]/a[1]')

    def click_add_farmer(self):
        self.page.click('button:has-text("Add Farmer")')

    def is_add_farmer_popup_visible(self):
        return self.page.is_visible('text=Add New Farmer')