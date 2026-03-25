from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self,page):
        self.page = page

    def confirm_Order(self, orderid):
        expect(self.page.locator("div.col-text.-main")).to_have_text(orderid)

    def click_ViewOrders(self):
        self.page.get_by_text("View Orders").click()
