from unicodedata import category
import requests
import json

baseUrl ='https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '012993441012'}
response = requests.get(baseUrl, params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
print(type(info))
print(info)
item=[info['items']]

itemInfo = item[0]
itemInfo = itemInfo[0]  # Access the first element of the list
category = itemInfo['category']
brand = itemInfo['brand']

print(category)
print(brand)
