from simplyhosting.client import Client
import unittest

class Test_user(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_auth_set_data_successfully(self):
        self.client.user().auth('benny', 'my-secret-password')
        request = self.client.request
        self.assertEqual('benny', request.data['login'])
        self.assertEqual('my-secret-password', request.data['password'])

    def test_ping_path_is_correct(self):
        self.client.user().ping()
        request = self.client.request
        self.assertEqual('/user/ping', request.path)