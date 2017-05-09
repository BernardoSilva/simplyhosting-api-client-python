import requests

def _url(path):
    return 'https://api.simplyhosting.com/v2' + path

def auth():
    return requests.post(_url('/user/auth'))

def ping():
    return requests.post(_url('/user/ping'))

def get_payment_methods():
    pass

def generate_secret_key():
    pass

def update_secret_key():
    pass

def delete_secret_key():
    pass

def get_secret_keys():
    pass

def regenerate_secret_key():
    pass