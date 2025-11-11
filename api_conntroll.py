import requests

url = "https://api.freeapi.app/api/v1/public/randomjokes"
#querystring = {"limit":"10","query":"science","inc":"categories%2Cid%2Ccontent","page":"1"}
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
#response = requests.get(url, headers=headers, params=querystring)
print(response.json())
       