import requests

res = requests.get("https://api.kanye.rest/")
print(res.json())
print(res.json()['quote'])