import requests
from config.config import API_KEY, URL


def get_weather(city: str):
    url = URL.format(city, API_KEY)

    response = requests.get(url)
    response = response.json()

    weather = response["weather"][0]["main"]
    temp = round(response["main"]["temp"] - 273.14, 1)

    return [weather, temp]

