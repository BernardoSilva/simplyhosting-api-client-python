from simplyhosting.client import Client
import unittest


class Test_support(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_get_active_tickets_set_all_fields_correctly(self):
        self.client.support().get_active_tickets(self.optional_data)

        request = self.client.request
        self.assertEqual('value', request.data['optionalParam'])

    def test_get_tickets_set_all_fields_correctly(self):
        self.client.support().get_tickets(20, self.optional_data)

        request = self.client.request
        self.assertEqual(20, request.data['limit'])
        self.assertEqual('value', request.data['optionalParam'])

    def test_search_set_all_fields_correctly(self):
        self.client.support().search(self.optional_data)
        request = self.client.request
        self.assertEqual('value', request.data['optionalParam'])

    def test_get_ticket_set_all_fields_correctly(self):
        self.client.support().get_ticket(69)
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])

    def test_reply_ticket_set_all_fields_correctly(self):
        self.client.support().reply_ticket(69, 'Done!')
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])
        self.assertEqual('Done!', request.data['text'])

    def test_update_ticket_priority_set_all_fields_correctly(self):
        self.client.support().update_ticket_priority(69, 2)
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])
        self.assertEqual(2, request.data['priority'])

    def test_close_ticket_set_all_fields_correctly(self):
        self.client.support().close_ticket(69)
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])

    def test_create_ticket_set_all_fields_correctly(self):
        ticket_subject = 'Server is down'
        ticket_body = 'The server has a network issue!'
        self.client.support().create_ticket(
            ticket_subject,
            ticket_body,
            self.optional_data
        )

        request = self.client.request
        self.assertEqual(ticket_subject, request.data['subject'])
        self.assertEqual(ticket_body, request.data['text'])
        self.assertEqual('value', request.data['optionalParam'])

    def test_update_ticket_set_all_fields_correctly(self):
        self.client.support().update_ticket(69, self.optional_data)
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])
        self.assertEqual('value', request.data['optionalParam'])

    def test_forward_to_ph_set_all_fields_correctly(self):
        self.client.support().forward_to_ph(69)
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])

    def test_forward_to_ph_remove_set_all_fields_correctly(self):
        self.client.support().forward_to_ph_remove(69)
        request = self.client.request
        self.assertEqual(69, request.data['ticketId'])
