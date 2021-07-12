import requests

BASE = "http://127.0.0.1:5000/"
response = requests.put(BASE + "helloworld/jeff", {"age": 15, })
print(response.json())   