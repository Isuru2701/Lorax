import os

from dotenv import load_dotenv
import requests
def makeCall(region):
    load_dotenv()

    key = os.getenv("WEATHER_API_KEY")
    # Geocode region
    geoUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={region}&limit=1&appid={key}"
    geoResponse = requests.get(geoUrl)

    data = geoResponse.json()
    lat = data[0]['lat']
    lon = data[0]['lon']

    #Get weather data
    weatherUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    weatherResponse = requests.get(weatherUrl)
    weather = weatherResponse.json()
    try:
        return weather['wind']['speed'], weather['rain']['1h']

    except:
        return weather['wind']['speed'], 0

