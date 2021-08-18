import requests

from config.user import user
from settings import BASE_URL


# get token to initiate a session
def get_token():
    response = requests.post(f"{BASE_URL}/v2/sessions", user)
    get_credentials = response.json()
    token = get_credentials["credentials"]["token"]
    return 'Bearer ' + token
