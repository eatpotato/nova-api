import pycurl, json
import requests

def get_token():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    url = 'http://controller:5000/v2.0/tokens'
    data = '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "d4fb1c91fc5549fd"}}}'
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access']['token']['id']


def index(project_id, server_name, image_ref, flavor_ref, network_id):
    url = 'http://controller:8774/v2/%s/servers' % project_id
    data = json.dumps({"server":  {"name": server_name, "imageRef": image_ref, "flavorRef": flavor_ref, "networks": [{"uuid": network_id}]}})
    token = str(get_token())
    try:
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, ['X-Auth-Token: %s' % token, 'Accept: application/json', 'Content-Type: application/json', 'User-Agent: python-novaclient'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.perform()
    except Exception as e:
        print e
    finally:
        c.close()

if __name__ == '__main__':
    index('321c7446162e431f91c69b60e64d605f', 'test-1', '394031a9-b5df-475b-94aa-f18c680bb575', '1', 'ac93b13c-b0e5-4af5-943e-0b0377a56a80')
