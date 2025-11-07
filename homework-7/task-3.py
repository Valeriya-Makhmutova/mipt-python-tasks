import requests

params =  {"title": "foo", "body": "bar", "userId": 1}

response = requests.post('https://jsonplaceholder.typicode.com/posts', data=params)

print(response.json())