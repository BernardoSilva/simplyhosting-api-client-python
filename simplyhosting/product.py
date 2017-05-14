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
