# admin specific API endpoints

class Admin(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def find_server(self, product_id, **kwargs):
        request = Request('post', '/admin/auth')
        request.data = {'productId': product_id}
        config_options = kwargs.get('config_options', '')
        if config_options:
            request.data['configOptions'] = config_options

        self.apiClient.request = request
        return self.apiClient

    def delegate_server(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def set_user_preference(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def get_opsview_notification_emails(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def get_opsview_checks(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def get_server_details(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def get_order_product(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def get_start_blacklist_check_for_ip(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient

    def get_start_blacklist_check_for_subnet(self):
        request = Request('post', '/admin/auth')
        self.apiClient.request = request
        return self.apiClient