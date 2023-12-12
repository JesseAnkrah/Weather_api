import requests

API_KEY = 'ce965a163d729883d7494b4b5fa5ac57'

print("this is a weather checker for the united states please follow the directions below")

def zip_code_func():
    location_zip = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}')
    location_zip_json = location_zip.json()
    longitude = location_zip_json['lon']
    latitude = location_zip_json['lat']

    cur_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial')
    cur_weather_json = cur_weather.json()
    
    cur_temp = cur_weather_json['main']['temp']
    cur_feels_like = cur_weather_json['main']['feels_like']
    cur_temp_max = cur_weather_json['main']['temp_max']
    cur_temp_min = cur_weather_json['main']['temp_min']

    print(cur_weather_json)
    print(f"The location you chose is {location_zip_json['name']}")
    print(f"this weather today will be {cur_temp} degrees farienheight and it feels like {cur_feels_like}")

def city_name_func():
    location_name = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},US&appid={API_KEY}')
    location_name_json = location_name.json()
   
    longitude = location_name_json[0]['lon']
    latitude = location_name_json[0]['lat']
    
    

    cur_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial')
    cur_weather_json = cur_weather.json()
    print(cur_weather_json)
    cur_temp = cur_weather_json['main']['temp']
    cur_feels_like = cur_weather_json['main']['feels_like']
    cur_temp_max = cur_weather_json['main']['temp_max']
    cur_temp_min = cur_weather_json['main']['temp_min']

    print(f"The location you chose is {cur_weather_json['name']}")
    print(f"The weather today will be a high of {cur_temp_max} degrees farienheight and a low of {cur_temp_min}")



mode = input("type \"zip\" to search by zip code or type \"name\" to seach by city name: ")

if mode == "zip":
    zip_code = input("please enter the zip code of the location you wish to check the weather in: ")
    zip_code_func()
elif mode == "name":
    city_name = input("please enter the name of the location you wish to check the weather in: ")
    state_code = input("what is the state? 2 letter abreviations only!: ")
    city_name_func()
else: exit()

















