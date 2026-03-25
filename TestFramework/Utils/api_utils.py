
from playwright.sync_api import Playwright

class APIUtils:

    def get_token(self, playwright: Playwright, user_data):
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        endpoint = "/api/ecom/auth/login"
        response = api_context.post(url=endpoint,data=user_data)
        assert response.status == 200
        response_body = response.json()
        print(response_body)
        token = response_body["token"]
        return token

    def create_order(self, playwright:Playwright, user_data):
        token= self.get_token(playwright, user_data)
        endpoint = "/api/ecom/order/create-order"
        order_payload = {"orders":[{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"},{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_context.post(url=endpoint,
                                    data=order_payload,
                                    headers={"Authorization": token,
                                             "Content-Type": "application/json"
                                             })
        assert response.status==201
        response_body = response.json()
        print(response_body)
        order_id = response_body["orders"]
        return order_id
