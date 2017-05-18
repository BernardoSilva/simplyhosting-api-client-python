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
        self._cache = kwargs.get('cache', [])

        if not (self.username and self.password):
            if not (self.api_key and self.api_secret):
                raise ValueError(
                    'Either (username, password) or (api_key, api_secret)'
                    ' kwargs combination are required'
                )

    def _(self, name):
        """build cache with uri parts.
        This method enabled method chaining and keeps authentication 
        details for new instance of Client()
        """
        return Client(
            cache=self._cache+[name],
            api_key=self.api_key,
            api_secret=self.api_secret,
            username=self.username,
            password=self.password
        )

    def __getattr__(self, name):
        """Reflection that avoid recursive loop during method chaining"""
        return self._(name)

    def _generate_token(self):
        """Generate new token with existing credentials
        @todo if there is no key/secret, client should attempt to get a 
        key with username/password and use that temporary token.
        """
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

    def _get_path(self):
        path = ''
        for part in self._cache:
            path += '/' + part
        return path

    def _url(self, path):
        return self.host + path + '?api_key=' + self._generate_token()

    def post(self):
        self.call('post')

    def get(self):
        self.call('get')

    def call(self, method_type, data={}, params={}):
        """Final method to be called to perform the request that was built"""
        requests_method = getattr(requests, method_type)
        requests_response = requests_method(
            self._url(self._get_path()),
            data=data,
            params=params,
            verify=False
        )

        return Response(requests_response)
