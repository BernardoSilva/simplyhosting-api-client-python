import os
import requests
import hashlib
import time
from .user import User
from .response import Response


class Client(object):
    """Simply Hosting apiI."""
    def __init__(self, *args, **kwargs):
        """
        Construct Simply Hosting API object.
        """
        # @todo client has to require either (username,password) or (api_key, api_secret)
        self.api_key = kwargs.get('api_key', '')
        self.api_secret = kwargs.get('api_secret', '')
        self.host = kwargs.get('host', 'https://api.simplyhosting.com/v2')
        self.request = ''
        self.api_version = 'v2'
        print('HOST:', self.host)


    def _generate_token(self):
        timestamp = int(time.time())
        hash_object = hashlib.sha256(self.api_secret + "-" + str(timestamp) + "-" + str(self.api_key))
        return str(self.api_key) +"-"+ hash_object.hexdigest() +"-"+ str(timestamp)

    def _url(self, path):
        return self.host + path + '?api_key=' + self._generate_token()

    def call(self):
        """Final method to be called to perform the request that was built"""
        requests_method = getattr(requests, self.request.method_type)
        # Ensure we have a token to do the request
        # self.request.params['api_key'] = self._generate_token()
        print('calling with data:')
        print(self.request.data)
        print('Requesting endpoint: ', self._url(self.request.path))
        print('Request params: ', self.request.params)
        

        requests_response = requests_method(
            self._url(self.request.path),
            data=self.request.data,
            params=self.request.params
        )

        return Response(requests_response)

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
