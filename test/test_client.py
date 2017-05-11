from simplyhosting.client import Client
import unittest

class Test_client(unittest.TestCase):
    def test_client_api_key_attribute_is_required(self):
        with self.assertRaises(ValueError):
            client = Client()

    def test_client_api_keys_can_be_set(self):
        my_api_key = 'test-key'
        my_api_secret = 'my-secret'
        client = Client(api_key=my_api_key, api_secret=my_api_secret)
        self.assertEqual(my_api_key, client.api_key)
        self.assertEqual(my_api_secret, client.api_secret)

    def test_client_api_user_credentials_can_be_set(self):
        my_username = 'bsilva@names.co.uk'
        my_password = 'my-super-password'
        client = Client(username=my_username, password=my_password)
        self.assertEqual(my_username, client.username)
        self.assertEqual(my_password, client.password)

    def test_ip_method_return_ip_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.ip()
        self.assertEqual('IP', api_resource.__class__.__name__)

    def test_os_method_return_os_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.os()
        self.assertEqual('OS', api_resource.__class__.__name__)

    def test_product_method_return_product_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.product()
        self.assertEqual('Product', api_resource.__class__.__name__)

    def test_r1soft_method_return_r1soft_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.r1soft()
        self.assertEqual('R1Soft', api_resource.__class__.__name__)

    def test_reseller_client_method_return_reseller_client_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.reseller_client()
        self.assertEqual('ResellerClient', api_resource.__class__.__name__)

    def test_reseller_vlan_method_return_reseller_vlan_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.reseller_vlan()
        self.assertEqual('ResellerVlan', api_resource.__class__.__name__)

    def test_server_method_return_server_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.server()
        self.assertEqual('Server', api_resource.__class__.__name__)

    def test_service_method_return_service_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.service()
        self.assertEqual('Service', api_resource.__class__.__name__)

    def test_support_method_return_support_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.support()
        self.assertEqual('Support', api_resource.__class__.__name__)

    def test_user_method_return_user_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.user()
        self.assertEqual('User', api_resource.__class__.__name__)

    def test_vlan_method_return_vlan_resource(self):
        client = Client(api_key='a', api_secret='b')
        api_resource = client.vlan()
        self.assertEqual('Vlan', api_resource.__class__.__name__)

if __name__ == '__main__':
    unittest.main(exit=False)