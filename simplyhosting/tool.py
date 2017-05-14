from .request import Request


class Tool(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def queue(self, id):
        request = Request('post', '/tool/queue')
        request.data = {'id': id}
        self.apiClient.request = request
        return self.apiClient
