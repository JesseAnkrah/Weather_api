import requests
# I also made this a repo on github this is the link: https://github.com/mugeltun/Weather_api

API_KEY = 'ce965a163d729883d7494b4b5fa5ac57'

print("this is a weather checker for the united states please follow the directions below")

def zip_code_func():
    zip_code = input("please enter the zip code of the location you wish to check the weather in: ")

    # 10.4 obtained json data from api
    location_zip = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}')
    location_zip_json = location_zip.json()
    
    # 10.5 extracted data from json and used the data 
    longitude = location_zip_json['lon']
    latitude = location_zip_json['lat']

    # 10.4 again
    cur_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial')
    cur_weather_json = cur_weather.json()
    
    # 10.5 again 
    cur_feels_like = cur_weather_json['main']['feels_like']
    cur_temp_max = cur_weather_json['main']['temp_max']
    cur_sky = cur_weather_json['weather'][0]['description']

    
    print(f"The location you chose is {cur_weather_json['name']}")
    print(f"The weather today will be a high of {cur_temp_max} degrees farienheight and it currently feels like {cur_feels_like}")
    print(f'with {cur_sky}')

def city_name_func():
    city_name = input("please enter the name of the location you wish to check the weather in: ")
    state_code = input("what is the state? 2 letter abreviations only!: ")

    # 10.4 obtained json data from api
    location_name = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},US&appid={API_KEY}')
    location_name_json = location_name.json()
   
    # 10.5 extracted data from json and used the data 
    longitude = location_name_json[0]['lon']
    latitude = location_name_json[0]['lat']

    # 10.4 again
    cur_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial')
    cur_weather_json = cur_weather.json()

    # 10.5 again 
    cur_feels_like = cur_weather_json['main']['feels_like']
    cur_temp_max = cur_weather_json['main']['temp_max']
    cur_sky = cur_weather_json['weather'][0]['description']


    print(f"The location you chose is {cur_weather_json['name']}")
    print(f"The weather today will be a high of {cur_temp_max} degrees farienheight and it currently feels like {cur_feels_like}")
    print(f'with {cur_sky}')

mode = input("type \"zip\" to search by zip code or type \"name\" to seach by city name: ")

if mode == "zip": zip_code_func()
elif mode == "name": city_name_func()
else: exit()

