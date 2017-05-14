from .request import Request


class IP(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def set_ptr(self, ip, optional_data={}):
        request = Request('post', '/ip/setPtr')
        request.data = {'ip': ip}
        request.data.update(optional_data)
        self.apiClient.request = request
        return self.apiClient

    def get_ptr(self, ip):
        request = Request('post', '/ip/getPtr')
        request.data = {'ip': ip}
        self.apiClient.request = request
        return self.apiClient
