from playwright.sync_api import expect

from TestFramework.pageObjects.orderDetails import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def click_View_Link(self,orderid):
        row = self.page.locator("tr").filter(has_text=orderid)
        row.get_by_role("button", name="View").click()
        orderdetailspage=OrderDetailsPage(self.page)
        return orderdetailspage

