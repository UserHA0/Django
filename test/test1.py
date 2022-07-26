import pprint
import requests

payload = {
    'username': 'userhao',
    'password': '123456'
}

response = requests.post('http://127.0.0.1:8000/api/mgr/signin',
                         data=payload)

pprint.pprint(response.json())
