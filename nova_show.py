import pycurl, json
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
    try:
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, ['X-Auth-Token: %s' % token, 'Accept: application/json', 'Content-Type: application/json', 'User-Agent: python-novaclient'])
        c.perform()
    except Exception as e:
        print e
    finally:
        c.close()

if __name__ == '__main__':
    index('321c7446162e431f91c69b60e64d605f', 'fdeb5519-58fa-4c23-83b3-23baa526db5f')
