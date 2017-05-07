import os


class Client(object):
    """Simply Hosting apiI."""
    def __init__(self, api_key, *args, **kwargs):
        """
        Construct Simply Hosting API object.
        """
        self.api_key = api_key
        self.host = kwargs.get('host', 'https://api.simplyhosting.com/v2')
