from simplyhosting.client import Client
import unittest


class Test_product(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_get_product_list_set_data_successfully(self):
        self.client.product().get_product_list(self.optional_data)
        request = self.client.request
        self.assertEqual('value', request.data['optionalParam'])
