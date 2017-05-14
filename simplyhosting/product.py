from .request import Request


class Product(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def get_product_list(self, optional_data={}):
        request = Request('post', '/product/getProductList')
        request.data.update(optional_data)
        self.apiClient.request = request
        return self.apiClient

    def get_config_options(self, product_id):
        request = Request('post', '/product/getConfigOptions')
        request.data = {'productId': product_id}
        self.apiClient.request = request
        return self.apiClient

    def get_addons(self, product_id):
        request = Request('post', '/product/getAddons')
        request.data = {'productId': product_id}
        self.apiClient.request = request
        return self.apiClient

    def order_product(self, product_id, optional_data={}):
        request = Request('post', '/product/orderProduct')
        request.data = {'productId': product_id}
        request.data.update(optional_data)
        self.apiClient.request = request
        return self.apiClient

    def order_products(self, product_id, payment_method, optional_data={}):
        request = Request('post', '/product/orderProducts')
        request.data = {'productId': product_id, 'paymentMethod': payment_method}
        request.data.update(optional_data)
        self.apiClient.request = request
        return self.apiClient

    def order_history(self, order_id):
        request = Request('post', '/product/orderHistory')
        request.data = {'orderId': order_id}
        self.apiClient.request = request
        return self.apiClient
