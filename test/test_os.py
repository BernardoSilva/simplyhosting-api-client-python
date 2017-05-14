from simplyhosting.client import Client
import unittest

class Test_os(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_get_params_set_data_successfully(self):
        self.client.os().get_params(1)
        request = self.client.request
        self.assertEqual(1, request.data['serverId'])