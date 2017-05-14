from .request import Request


class OS(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def get_params(self, server_id):
        request = Request('post', '/os/getParams')
        request.data = {'serverId': server_id}
        self.apiClient.request = request
        return self.apiClient

    def get_available_os_versions(self, server_id):
        request = Request('post', '/os/getAvailableOsVersions')
        request.data = {'serverId': server_id}
        self.apiClient.request = request
        return self.apiClient
