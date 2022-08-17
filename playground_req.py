import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
for i in response.history:
    print(i.url)
# 1 редирект, конечный url:https://playground.learnqa.ru/
