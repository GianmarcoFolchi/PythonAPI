import requests

BASE = "http://127.0.0.1:5000/"
print("Put: ")
response = requests.put(BASE + "helloworld/Nicolle", {"age": 15, "gender": "female", "email": "nicolle.folchi@hotmail.com"})
print(response.json())   
input()
print("Get: ")
response = requests.get(BASE + "helloworld/jeff")
print(response.json())   