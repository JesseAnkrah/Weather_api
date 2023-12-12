import requests

API_KEY = 'ce965a163d729883d7494b4b5fa5ac57'

zip_code = input("please enter the zipcode of the location you wish to check the weather in: ")


location = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}')
location_json = location.json()
longitude = location_json['lon']
latitude = location_json['lat']

cur_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial')
cur_weather_json = cur_weather.json()

cur_temp = cur_weather_json['main']['temp']
cur_feels_like = cur_weather_json['main']['feels_like']
cur_temp_max = cur_weather_json['main']['temp_max']
cur_temp_min = cur_weather_json['main']['temp_min']

print(f"The location you chose is {location_json['name']}")
print(cur_weather_json)
print(f"this weather today will be {cur_temp} degrees farienheight and it feels like {cur_feels_like}")