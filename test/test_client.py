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

    def test_client_user_method_return_user_resource(self):
        client = Client(api_key='a', api_secret='b')
        user_object = client.user()
        self.assertEqual('User', user_object.__class__.__name__)

if __name__ == '__main__':
    unittest.main(exit=False)