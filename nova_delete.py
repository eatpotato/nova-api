import requests

def get_token():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    url = 'http://controller:5000/v2.0/tokens'
    data = '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "d4fb1c91fc5549fd"}}}'
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access']['token']['id']


def index(project_id, instance_id):
    url = 'http://controller:8774/v2/%s/servers/%s' % (project_id, instance_id)
    token = str(get_token())
    headers = {'X-Auth-Token': token, 'Accept': 'application/json', 'Content-Type': 'application/json', 'User-Agent': 'python-novaclient'}
    r = requests.delete(url, headers=headers)

if __name__ == '__main__':
    index('321c7446162e431f91c69b60e64d605f', '70a494f5-d5e7-4aac-80bf-a6eb18876a4b')
