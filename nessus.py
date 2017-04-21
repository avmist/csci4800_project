import requests
import json
import getpass

base_url = ''
username = ''
password = ''
login = {}

class scan():
    def __init__(self,name,id):
        self.name = name
        self.id = id
def get_token():
    valid = True
    resp = requests.post(base_url+'/session',data=login,verify=False)
    return resp.json()['token']

def get_scans():
    ret_scans = []
    token = get_token()
    headers = {'X-Cookie': 'token=' + token, 'content-type': 'application/json'}
    resp = requests.get(base_url + '/scans', data=None, headers=headers, verify=False)
    scans = resp.json()['scans']
    for i in scans:
        ret_scans.append(scan(name=i['id'],id=i['id']))
    return ret_scans

def get_scan_data(id):
    token = get_token()
    headers = {'X-Cookie': 'token=' + token, 'content-type': 'application/json'}
    resp = requests.get(base_url + '/scans/' + str(id), data=None, headers=headers, verify=False)


if __name__ == '__main__':
    base_url = raw_input("Enter your base url for Nessus (e.g. https://10.10.10.10:8834): ")
    username = raw_input("Enter your login username: ")
    password = getpass.getpass("Enter your login password: ")
    login = {'username': username, 'password': password}