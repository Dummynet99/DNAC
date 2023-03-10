import requests
from requests.auth import HTTPBasicAuth

DNAC_URL = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PASS = "Cisco123!"

requests.packages.urllib3.disable_warnings()

def get_auth_token():
     """
     Building out Auth request. Using requests.post to make a call to the Auth Endpoint
     """
     url = 'https://{}/dna/system/api/v1/auth/token'.format(DNAC_URL)                                    # Endpoint URL
     hdr = {'content-type' : 'application/json'}                                                         # Define request header
     resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), headers=hdr, verify=False)      # Make the POST Request
     token = resp.json()['Token']                                                                        # Retrieve the Token
     print("Token Retrieved: {}".format(token))                                                          # Print out the Token
     return token                                                                                        # Create a return statement to send the token back for later use

def get_device_int():
    """
    Building out function to retrieve device interface. Using requests.get to make a call to the network device Endpoint
    """
    token = get_auth_token() # Get Token
    url = "https://{}/dna/intent/api/v1/interface".format(DNAC_URL)
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=hdr, verify=False)
    interface_info_json = resp.json()
    print_interface_info(interface_info_json)

def print_interface_info(interface_info):
    print("{0:27}{1:6}{2:15}{3:25}{4:17}{5:10}{6:15}{7:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "pid", "serial number"))
    for interface in interface_info['response']:
        print("{0:27}{1:6}{2:15}{3:25}{4:17}{5:10}{6:15}{7:15}".
              format(interface['portName'],
                     interface['vlanId'],
                     interface['portMode'],
                     interface['portType'],
                     interface['duplex'],
                     interface['status'],
                     interface['pid'],
                     interface['serialNo']))

if __name__ == "__main__":
    get_device_int()
