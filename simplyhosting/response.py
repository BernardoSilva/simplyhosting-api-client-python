class Response(object):
	"""wrapper class for requests.response object to facilitate response handling"""
	def __init__(self, requests_response):
		print('got requests_response object:', requests_response)
		self.content = requests_response.json()
		self.status_code = requests_response.status_code
		self.original_response = requests_response