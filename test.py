import requests

BASE = "http://127.0.0.1:5000/"

#Post: 
response = requests.post(BASE + "helloworld/Gianmarco", {"gender": "male", "email": "gmfolc@gmail.com", "age": 19})
print(response.json())
input()

#Patch:
response = requests.patch(BASE + "helloworld/Gianmarco", {"age": 20})
print(response.json())   
input()

#Get:
response = requests.get(BASE + "helloworld/Gianmarco")
print(response.json())   