import requests
import time
import json

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
job_create = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job").text
toxic = json.loads(job_create)

tok = toxic["token"]
job_check = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": tok})
print(job_check.text)

timer = toxic["seconds"]
time.sleep(timer)
job_over = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": tok}).text
print(job_over)

job_results = json.loads(job_over)
assert "42" in job_results["result"] and "Job is ready" in job_results["status"]