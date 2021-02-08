import requests
import json

result = requests.get('https://www.googleapis.com/books/v1/volumes?q=harry+potter')
print(result.status_code)
# print(result.text)

books = result.json()
print(type(books))

items = books["items"]

coded = json.dumps(items)
decoded = json.loads(coded)

print(decoded[0]["volumeInfo"]["infoLink"])