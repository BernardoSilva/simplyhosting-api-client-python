from simplyhosting.client import Client
import unittest


class Test_support(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')

    def test_support_create_ticket_set_all_fields_correctly(self):
        ticket_subject = 'Server is down'
        ticket_body = 'The server has a network issue!'
        self.client.support().create_ticket(
            ticket_subject,
            ticket_body,
            server_id=123,
            service_id=1234,
            cc='group@email.com',
            priority=2,
            type=4
        )

        request = self.client.request
        self.assertEqual(ticket_subject, request.data['subject'])
        self.assertEqual(ticket_body, request.data['text'])
        self.assertEqual(123, request.data['serverId'])
        self.assertEqual(1234, request.data['serviceId'])
        self.assertEqual('group@email.com', request.data['cc'])
        self.assertEqual(2, request.data['priority'])
        self.assertEqual(4, request.data['type'])