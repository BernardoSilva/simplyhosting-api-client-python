from simplyhosting.Client import Client
import unittest

class Test_client(unittest.TestCase):
	def test_client_api_key_attribute_is_required(self):
		with self.assertRaises(TypeError):
			client = Client()

	def test_client_api_key_can_be_set(self):
		my_api_key = 'test-key'
		client = Client(my_api_key)
		self.assertEqual(my_api_key, client.api_key)	

if __name__ == '__main__':
	unittest.main(exit=False)