import requests
import mysql.connector

def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def insert_weather_data(weather_data):
        query = "INSERT INTO weather (country, temperature) VALUES (%s, %s)"
        values = (weather_data['sys']['country'], weather_data['main']['temp'])
        cursor.execute(query, values)
        cnx.commit()

# for testing purposes only, delete later
def print_table():
    query = "SELECT * FROM weather"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
            print(row)

#Establish a connection to the mysql database
try:
    cnx = mysql.connector.connect(
     host="host",
     user="user",
     password="password",
     database="database"
    )
    cursor = cnx.cursor()
except Exception:
    print("mysql.connector failed! could not connect to mysql database")

# hardcoded for now
api_key = 'ccb58c269cfb807b9f52f1600b47ceae'
lat = 44.34
lon = 11.99

try:
    weather_data = get_weather(api_key, lat, lon)
    print(weather_data)
    print("\n\n")
    print(weather_data['sys']['country'])
    print("\n\n")
    print(weather_data['main']['temp'])
except Exception:
    print("get_weather function failed!")
