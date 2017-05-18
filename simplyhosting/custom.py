from .request import Request


class Custom(object):
    """Resource that will allow developer to create custom requests to the API
    This should only be used for API endpoints not docummented or supported.
    """
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def request(self, path, method_type='post', optional_data={}):
        request = Request(method_type, path)
        request.data = optional_data
        self.apiClient.request = request
        return self.apiClient
