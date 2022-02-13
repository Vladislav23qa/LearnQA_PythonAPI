import requests

headers = {"some_header":"123456"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
print(response.text)