import requests

params = {"name": "Dmitriy"}
response = requests.get('https://playground.learnqa.ru/api/hello', params=params)
parsed_response_text = response.json()
print(parsed_response_text["answer"])
