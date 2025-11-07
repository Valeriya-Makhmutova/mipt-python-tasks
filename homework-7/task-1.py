import requests

# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# # print(response.json())
# res_json = response.json()

try:
  response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.json())
  res_json = response.json()
  i = 0
  for element in res_json:
    if i > 4:
      break
    print(f"Title: {element['title']} \nBody: {element['body']}")
    i += 1
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при запросе: {e}")

# i = 0
# for element in res_json:
#   if i > 4:
#     break
#   print(f"Title: {element['title']} \nBody: {element['body']}")
#   i += 1
  