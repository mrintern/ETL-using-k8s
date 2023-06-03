import requests
import mysql.connector

def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# hardcoded for now
api_key = 'ccb58c269cfb807b9f52f1600b47ceae'
lat = 44.34
lon = 11.99

try:
    weather_data = get_weather(api_key, lat, lon)
    print(weather_data)
except NameError:
    print("NameError! oh no!")
