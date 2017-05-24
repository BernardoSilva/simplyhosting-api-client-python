import os
import requests
import hashlib
import time
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
        # ensure we always work with values instead of tuples
        if type(self.username) == tuple:
            self.username = self.username[0]
        if type(self.password) == tuple:
            self.password = self.password[0]
        if type(self.api_key) == tuple:
            self.api_key = self.api_key[0]
        if type(self.api_secret) == tuple:
            self.api_secret = self.api_secret[0]

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
            password=self.password,
            host=self.host
        )

    def __getattr__(self, name):
        """Reflection that avoid recursive loop during method chaining"""
        return self._(name)

    def _generate_token(self, **kwargs):
        """Generate new token with existing credentials
        @todo if there is no key/secret, client should attempt to get a
        key with username/password and use that temporary token.
        """
        current_timestamp = kwargs.get('current_timestamp', time.time())
        timestamp = int(current_timestamp)
        hash_object = hashlib.sha256(
            str(self.api_secret).encode('utf-8') +
            '-'.encode('utf-8') +
            str(timestamp).encode('utf-8') +
            '-'.encode('utf-8') +
            str(self.api_key).encode('utf-8')
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

    def post(self, data={}):
        return self.call('post', data=data)

    def get(self, params={}):
        return self.call('get', params=params)

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
