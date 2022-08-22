import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
for i, each in enumerate(response.history, 1):
    print({i},  {each.status_code}, {each.url}, response.url)
