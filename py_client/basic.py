import requests

endpoint = 'http://127.0.0.1:8000/api'

res = requests.get(endpoint, json={'name': 'Davis Ochieng'}, params={'abc': 123})
print(res.json())