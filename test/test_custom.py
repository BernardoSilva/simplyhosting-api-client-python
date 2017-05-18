from simplyhosting.client import Client
import unittest

class Test_Custom(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_request_set_data_successfully(self):
        self.client.custom().request('/vlan/addServer', 'post', {'serverId':1, 'vlanSid': 3})
        request = self.client.request
        self.assertEqual('/vlan/addServer', request.path)
        self.assertEqual('post', request.method_type)
        self.assertEqual(1, request.data['serverId'])
        self.assertEqual(3, request.data['vlanSid'])
