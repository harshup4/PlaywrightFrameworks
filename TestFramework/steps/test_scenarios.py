import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from TestFramework.Utils.api_utils import APIUtils
from TestFramework.pageObjects.login import LoginPage

scenarios('../features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place order with {username} and {password}'))
def place_order(playwright, username, password, shared_data):
    user_credentials = {}
    api_utils = APIUtils()
    user_credentials["userEmail"]=username
    user_credentials["userPassword"] = password
    list_order_ids = api_utils.create_order(playwright, user_credentials)
    shared_data['list_order_ids'] = list_order_ids


@given('user is on landing page')
def user_on_landing_page(browser_instance,shared_data):
    page = browser_instance
    loginPage = LoginPage(page)
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse('user login to portal with {username} and {password}'))
def user_login(username, password,shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboard_Page'] = dashboardPage

@when('navigate to Orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_Page']
    orderHistoryPage = dashboardPage.click_OrderLink()
    shared_data['orderHistory_Page'] = orderHistoryPage

@then('Select order and verify order id')
def select_order_and_verify_order_id(shared_data):
    list_order_ids = shared_data['list_order_ids']
    orderHistoryPage = shared_data['orderHistory_Page']
    for orderid in list_order_ids:
        orderdetailspage = orderHistoryPage.click_View_Link(orderid)
        orderdetailspage.confirm_Order(orderid)
        orderdetailspage.click_ViewOrders()