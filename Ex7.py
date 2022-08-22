import requests
import urllib3

r = urllib3.PoolManager()
response = r.request("https://playground.learnqa.ru/ajax/api/compare_query_type", {"method": 'GET'})
print(response)
