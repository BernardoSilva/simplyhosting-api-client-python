from simplyhosting.client import Client
import unittest


class Test_tool(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')

    def test_queue_set_data_successfully(self):
        self.client.tool().queue(1)
        request = self.client.request
        self.assertEqual(1, request.data['id'])
