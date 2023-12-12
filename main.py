import requests

API_KEY = 'ce965a163d729883d7494b4b5fa5ac57'

zip_code = input("please enter the zipcode of the location you wish to check the weather in: ")


location_request = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}')
location_request_json = location_request.json()
longitude = location_request_json['lat']
latitude = location_request_json['lon']

print(latitude,longitude)