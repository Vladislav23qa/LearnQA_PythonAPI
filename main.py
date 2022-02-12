import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
response1 = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
print(response1)