import os
import requests
import hashlib
import time
from .ip import IP
from .os import OS
from .product import Product
from .r1soft import R1Soft
from .reseller_client import ResellerClient
from .reseller_server import ResellerServer
from .reseller_vlan import ResellerVlan
from .server import Server
from .service import Service
from .support import Support
from .tool import Tool
from .user import User
from .vlan import Vlan
from .custom import Custom
from .response import Response


class Client(object):
    """Simply Hosting apiI."""
    def __init__(self, *args, **kwargs):
        """
        Construct Simply Hosting API object.
        """
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.api_key = kwargs.get('api_key', '')
        self.api_secret = kwargs.get('api_secret', '')
        self.host = kwargs.get('host', 'https://api.simplyhosting.com/v2')
        self.request = ''
        self.api_version = 'v2'

        if not (self.username and self.password):
            if not (self.api_key and self.api_secret):
                raise ValueError(
                    'Either (username, password) or (api_key, api_secret)'
                    ' kwargs combination are required'
                )

    def _generate_token(self):
        timestamp = int(time.time())

        hash_object = hashlib.sha256(
            self.api_secret + '-' + str(timestamp) + '-' + str(self.api_key)
        )
        token = (
            str(self.api_key) + '-' +
            hash_object.hexdigest() + '-' +
            str(timestamp)
        )
        return token

    def _url(self, path):
        return self.host + path + '?api_key=' + self._generate_token()

    def call(self):
        """Final method to be called to perform the request that was built"""
        requests_method = getattr(requests, self.request.method_type)
        requests_response = requests_method(
            self._url(self.request.path),
            data=self.request.data,
            params=self.request.params,
            verify=False
        )

        return Response(requests_response)

    # Client helper methods
    def authenticate_with_username_password(self, username, password):
        response = self.user().auth(username, password).call()
        json_response = response.json()
        self.api_key = json_response['response'][0]['api_key']
        self.api_version = json_response['response'][0]['api_version']

    # API Resources available
    def ip(self):
        return IP(self)

    def os(self):
        return OS(self)

    def product(self):
        return Product(self)

    def r1soft(self):
        return R1Soft(self)

    def reseller_client(self):
        return ResellerClient(self)

    def reseller_vlan(self):
        return ResellerVlan(self)

    def server(self):
        return Server(self)

    def service(self):
        return Service(self)

    def support(self):
        return Support(self)

    def tool(self):
        return Tool(self)

    def user(self):
        return User(self)

    def vlan(self):
        return Vlan(self)

    def custom(self):
        return Custom(self)
