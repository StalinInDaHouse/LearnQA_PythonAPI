import requests

first_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(first_response.text)

second_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "POST"})
print(second_response.text)

third_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(third_response.text)

param = [{"j": {"method": "GET"}}, {"j": {"method": "POST"}}, {"j": {"method": "PUT"}}, {"j": {"method": "PATCH"}},
         {"j": {"method": "DELETE"}}, {"j": {"method": "OPTIONS"}}, {"j": {"method": "HEAD"}}]
for i in param:
    cicle_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in GET request")
for i in param:
    cicle_response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in POST request")
for i in param:
    cicle_response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in PUT request")
for i in param:
    cicle_response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in PATCH request")
for i in param:
    cicle_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in DELETE request")
for i in param:
    cicle_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in OPTIONS request")
for i in param:
    cicle_response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i["j"])
    print(f"{cicle_response.text} for {param.index(i)} in HEAD request")