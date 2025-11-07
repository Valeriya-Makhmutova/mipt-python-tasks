import requests

user_city = input('Введите город, в котором хотите узнать погоду (на английском, с большой буквы): ')
print(user_city)
# https://api.weatherapi.com/v1/current.json?key=59f4413edfef45538e291852250711&q=London&aqi=yes
url_start_part = "https://api.weatherapi.com/v1vftgyhujikocdrfvtgyhuj/current.json?key=59f4413edfef45538e291852250711"
url=f"{url_start_part}&q={user_city}&aqi=yes"


try:
    response = requests.get(url)
    response.raise_for_status()
    result = f"Температура воздуха в градусах по Цельсию: {response.json()['current']['temp_c']}"
    print(result)
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при запросе: {e}")



# if response.ok != True:
#   print()



# print(result)
# print(response.status_code)
# print(response.text)
# print(response.reason)

