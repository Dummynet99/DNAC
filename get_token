import env_lab
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()


def get_token(host=env_lab.DNA_CENTER['host'],
              username=env_lab.DNA_CENTER['username'],
              password=env_lab.DNA_CENTER['password'],
              port=env_lab.DNA_CENTER['port']):

    url = f'https://{host}:{port}/dna/system/api/v1/auth/token'
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), verify=False)
    token = response.json()["Token"]
    return token

token = get_token()
print(token)
