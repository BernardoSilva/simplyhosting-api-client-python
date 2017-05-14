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

    def test_get_payment_method_path_is_correct(self):
        self.client.user().get_payment_methods()
        request = self.client.request
        self.assertEqual('/user/getPaymentMethods', request.path)

    def test_generate_secret_key_set_data_successfully(self):
        self.client.user().generate_secret_key('dev-key', 'rw')
        request = self.client.request
        self.assertEqual('dev-key', request.data['keyName'])
        self.assertEqual('rw', request.data['access'])

    def test_update_secret_key_set_data_successfully(self):
        self.client.user().update_secret_key(1, self.optional_data)
        request = self.client.request
        self.assertEqual(1, request.data['keyId'])
        self.assertEqual('value', request.data['optionalParam'])
