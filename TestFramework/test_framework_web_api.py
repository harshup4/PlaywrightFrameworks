import pytest

from TestFramework.Utils.api_utils import APIUtils
from playwright.sync_api import Playwright, expect
from TestFramework.Utils.file_utils import read_file
from TestFramework.pageObjects.dashboard import DashboardPage
from TestFramework.pageObjects.login import LoginPage

user_credentials_list = read_file()["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_api_web(browser_instance, playwright:Playwright, user_credentials):
    page=browser_instance
    email = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    api_utils = APIUtils()
    list_order_ids = api_utils.create_order(playwright, user_credentials)
    print(list_order_ids)
    loginPage = LoginPage(page)
    loginPage.navigate()
    dashboardPage = loginPage.login(email, password)
    dashboardPage.check_pageTitle()
    orderHistoryPage = dashboardPage.click_OrderLink()
    for orderid in list_order_ids:
        orderdetailspage = orderHistoryPage.click_View_Link(orderid)
        orderdetailspage.confirm_Order(orderid)
        orderdetailspage.click_ViewOrders()

