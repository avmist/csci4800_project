import requests
import json
import getpass

login = {} # JSON object for requesting token

# initialize login JSON object for requesting token
def login(ip,un,pw,port):
    base_url = 'https://' + ip + ':' + port
    login = {'username':un,'password':pw}

# get token with login
def get_token():
    resp = requests.post(base_url+'/session',data=login,verify=False)
    return resp.json()['token']

# get a list of all scans
def get_scans():
    scan_names = []
    token = get_token()
    headers = {'X-Cookie': 'token=' + token, 'content-type': 'application/json'}
    scans = requests.get(base_url + '/scans', data=None, headers=headers, verify=False).json()['scans']
    for scan in scans:
        scan_names.append(scan['name'])
    return scan_names

# given a scan name, get a list of all items in that scan
def get_scan_data(name):
    scan_items = []
    token = get_token()
    headers = {'X-Cookie': 'token=' + token, 'content-type': 'application/json'}
    scans = requests.get(base_url + '/scans', data=None, headers=headers, verify=False).json()['scans']
    for scan in scans:
        if scan['name'] == name:
            id = scan['id']
    scan_data = requests.get(base_url + '/scans/' + str(id), data=None, headers=headers, verify=False)
    for scan_item in scan_data:
        scan_items.append(scan_item)
