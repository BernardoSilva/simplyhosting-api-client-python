from .request import Request


class User:
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def auth(self, username, password):
        """authenticate the user"""
        request = Request('post', '/user/auth')
        request.data = {'login': username, 'password': password}
        self.apiClient.request = request
        return self.apiClient

    def ping(self):
        """health check to see if API is working and user is authenticated"""
        request = Request('post', '/user/ping')
        self.apiClient.request = request
        return self.apiClient

    def get_payment_methods(self):
        pass

    def generate_secret_key(self):
        pass

    def update_secret_key(self):
        pass

    def delete_secret_key(self):
        pass

    def get_secret_keys(self):
        pass

    def regenerate_secret_key(self):
        pass
