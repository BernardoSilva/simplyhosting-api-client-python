from simplyhosting.client import Client
import unittest

class Test_vlan(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_add_server_set_data_successfully(self):
        self.client.vlan().add_server(1, 3)
        request = self.client.request
        self.assertEqual(1, request.data['serverId'])
        self.assertEqual(3, request.data['vlanSid'])

    def test_remove_server_set_data_successfully(self):
        self.client.vlan().remove_server(1, 3)
        request = self.client.request
        self.assertEqual(1, request.data['serverId'])
        self.assertEqual(3, request.data['vlanSid'])
