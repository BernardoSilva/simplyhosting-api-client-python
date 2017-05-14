from .request import Request


class Vlan(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def add_server(self, server_id, vlan_sid):
        request = Request('post', '/vlan/addServer')
        request.data = {'serverId': server_id, 'vlanSid': vlan_sid}
        self.apiClient.request = request
        return self.apiClient

    def remove_server(self, server_id, vlan_sid):
        request = Request('post', '/vlan/removeServer')
        request.data = {'serverId': server_id, 'vlanSid': vlan_sid}
        self.apiClient.request = request
        return self.apiClient

    def list(self):
        request = Request('post', '/vlan/list')
        self.apiClient.request = request
        return self.apiClient
