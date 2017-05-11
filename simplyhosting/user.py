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
        request = Request('post', '/user/getPaymentMethods')
        self.apiClient.request = request
        return self.apiClient

    def generate_secret_key(self, key_name, access):
        request = Request('post', '/user/generateSecretKey')
        request.data = {}
        key_name = kwargs.get('key_name', '')
        access = kwargs.get('access', '')
        if key_name:
            request.data['keyName'] = key_name

        if access:
            request.data['access'] = access
        self.apiClient.request = request
        return self.apiClient

    def update_secret_key(self, key_id, **kwargs):
        request = Request('post', '/user/updateSecretKey')
        request.data = {'keyId': key_id}
        key_name = kwargs.get('key_name', '')
        access = kwargs.get('access', '')
        if key_name:
            request.data['keyName'] = key_name

        if access:
            request.data['access'] = access

        self.apiClient.request = request
        return self.apiClient

    def delete_secret_key(self, key_id):
        request = Request('post', '/user/deleteSecretKey')
        request.data = {'keyId': key_id}
        self.apiClient.request = request
        return self.apiClient

    def get_secret_keys(self):
        request = Request('post', '/user/getSecretKeys')
        self.apiClient.request = request
        return self.apiClient

    def regenerate_secret_key(self, key_identifier, access):
        request = Request('post', '/user/regenerateSecretKey')
        request.data = {'keyId': key_identifier, 'access': access}
        self.apiClient.request = request
        return self.apiClient
