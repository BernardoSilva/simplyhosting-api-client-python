class Request(object):
    def __init__(self, method_type, path):
        self.method_type = method_type
        self.path = path
        self.params = {}
        self.data = {}
