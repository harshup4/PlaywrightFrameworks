from playwright.sync_api import expect
from TestFramework.pageObjects.orderHistory import OrderHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def check_pageTitle(self):
        expect(self.page).to_have_title("Let's Shop")

    def click_OrderLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistoryPage = OrderHistoryPage(self.page)
        return orderHistoryPage