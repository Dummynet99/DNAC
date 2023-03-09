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

def get_commands(token, host=env_lab.DNA_CENTER['host'], port=env_lab.DNA_CENTER['port']):
    url = f'https://{host}:{port}/api/v1/network-device-poller/cli/legit-reads'
    headers = {
        "X-Auth-Token": token
        }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    print(f'Exec commands supported:', json.dumps(response.json()['response'], indent=4))

if __name__ == '__main__':
    token = get_token()
    print(f'\n\nDNA-C Authentication token: {token}\n\n')
    pause = input('Press Enter to display Command Runner Commands:')
    get_commands(token)
