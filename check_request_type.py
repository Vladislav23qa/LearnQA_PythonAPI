import requests

response = requests.put("https://playground.learnqa.ru/api/check_type",data ={"param1":"VALue1"})
print(response.text)