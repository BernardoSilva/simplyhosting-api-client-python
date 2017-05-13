from simplyhosting.client import Client
import unittest


class Test_support(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')

    def test_get_active_tickets_set_all_fields_correctly(self):
        self.client.support().get_active_tickets(
            client_id=1,
            from_date='2017-05-13',
            to_date='2017-05-15',
            server_id=2,
            service_id=3,
            status=0
        )

        request = self.client.request
        self.assertEqual(1, request.data['clientId'])
        self.assertEqual('2017-05-13', request.data['fromDate'])
        self.assertEqual('2017-05-15', request.data['toDate'])
        self.assertEqual(2, request.data['serverId'])
        self.assertEqual(3, request.data['serviceId'])
        self.assertEqual(0, request.data['status'])

    def test_get_tickets_set_all_fields_correctly(self):
        self.client.support().get_tickets(
            20,
            client_id=1,
            from_date='2017-05-13',
            to_date='2017-05-15',
            server_id=2,
            service_id=3,
            status=0
        )

        request = self.client.request
        self.assertEqual(20, request.data['limit'])
        self.assertEqual(1, request.data['clientId'])
        self.assertEqual('2017-05-13', request.data['fromDate'])
        self.assertEqual('2017-05-15', request.data['toDate'])
        self.assertEqual(2, request.data['serverId'])
        self.assertEqual(3, request.data['serviceId'])
        self.assertEqual(0, request.data['status'])

    def test_search_set_all_fields_correctly(self):
        self.client.support().search(
            from_date='2017-05-13',
            to_date='2017-05-15',
            server_id=2,
            client_id=1,
            server_label='dev',
            text='example'
        )

        request = self.client.request
        self.assertEqual('2017-05-13', request.data['fromDate'])
        self.assertEqual('2017-05-15', request.data['toDate'])
        self.assertEqual(2, request.data['serverId'])
        self.assertEqual(1, request.data['clientId'])
        self.assertEqual('dev', request.data['server_label'])
        self.assertEqual('example', request.data['text'])

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