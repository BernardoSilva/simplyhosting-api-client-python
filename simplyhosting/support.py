from .request import Request


class Support(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def get_active_tickets(self, **kwargs):
        request = Request('post', '/support/getActiveTickets')
        client_id = kwargs.get('client_id', '')
        from_date = kwargs.get('from_date', '')
        to_date = kwargs.get('to_date', '')
        server_id = kwargs.get('server_id', '')
        service_id = kwargs.get('service_id', '')
        status = kwargs.get('status', '')

        if client_id:
            request.data['clientId'] = client_id
        if from_date:
            request.data['fromDate'] = from_date
        if to_date:
            request.data['toDate'] = to_date
        if server_id:
            request.data['serverId'] = server_id
        if service_id:
            request.data['serviceId'] = service_id

        self.apiClient.request = request
        return self.apiClient

    def get_tickets(self):
        pass

    def search(self):
        pass

    def get_ticket(self):
        pass

    def reply_ticket(self):
        pass

    def update_ticket_priority(self):
        pass

    def close_ticket(self):
        pass

    def create_ticket(self, subject, text, **kwargs):
        request = Request('post', '/support/createTicket')
        request.data = {'subject': subject, 'text': text}

        server_id = kwargs.get('server_id', '')
        service_id = kwargs.get('service_id', '')
        cc = kwargs.get('cc', '')
        priority = kwargs.get('priority', '')
        ticket_type = kwargs.get('type', '')

        if service_id:
            request.data['serviceId'] = service_id
        if server_id:
            request.data['serverId'] = server_id
        if cc:
            request.data['cc'] = cc
        if priority:
            request.data['priority'] = priority
        if ticket_type:
            request.data['type'] = ticket_type

        self.apiClient.request = request
        return self.apiClient

    def update_ticket(self):
        pass

    def forward_to_ph(self):
        pass

    def forward_to_ph_remove(self):
        pass
