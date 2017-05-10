import os
import requests
from .user import User


class Client(object):
    """Simply Hosting apiI."""
    def __init__(self, api_key, *args, **kwargs):
        """
        Construct Simply Hosting API object.
        """
        self.api_key = api_key
        self.host = kwargs.get('host', 'https://api.simplyhosting.com/v2')
        self.request = ''
        self.api_version = 'v2'

    def _url(self, path):
        return 'https://api.simplyhosting.com/v2' + path

    def call(self):
        """Final method to be called to perform the request that was built"""
        requests_method = getattr(requests, self.request.method_type)
        print('calling with data:')
        print(self.request.data)
        return requests_method(self._url(self.request.path), data = self.request.data)

    # Client helper methods
    def authenticate_with_username_password(self, username, password):
        response = self.user().auth(username, password).call()
        json_response = response.json()
        print(json_response['response'][0])
        print('errorMessage: '+json_response['response'][0]['errorMessage'])
        print('status: '+json_response['response'][0]['status'])
        self.api_key = json_response['response'][0]['api_key']
        self.api_version = json_response['response'][0]['api_version']

    # API Resources available
    def ip(self):
        pass

    def os(self):
        pass

    def product(self):
        pass

    def r1Soft(self):
        pass

    def resellerClient(self):
        pass

    def resellerVlan(self):
        pass

    def server(self):
        pass

    def service(self):
        pass

    def support(self):
        pass

    def user(self):
        return User(self)

    def vlan(self):
        pass
