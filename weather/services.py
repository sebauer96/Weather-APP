import requests
import json


def get_weathers_accuweather(latitude, longitude):
    url = 'http://127.0.0.1:5000/accuweather'
    params = {'latitude': latitude, 'longitude': longitude}
    req = requests.get(url, params=params)
    weather_json = req.json()
    weather = {}
    weather['temperature'] = (int(weather_json['simpleforecast']['forecastday'][0]['high']['celsius']) +
                              int(weather_json['simpleforecast']['forecastday'][0]['low']['celsius'])) / 2
    weather['service'] = "accuweather"
    weather['latitude'] = latitude
    weather['longitude'] = longitude
    weather['img'] = weather_json['simpleforecast']['forecastday'][0]["icon_url"]
    return weather


def get_weathers_noaa(latlon):
    url = 'http://127.0.0.1:5000/noaa'
    params = {'latlon': latlon}
    req = requests.get(url, params=params)
    weather_json = req.json()
    weather = {}
    weather['temperature'] = (int(weather_json['today']['high']['celsius']) +
                              int(weather_json['today']['low']['celsius'])) / 2
    weather['service'] = "noaa"
    weather['latitude'] = latlon.split(',')[0]
    weather['longitude'] = latlon.split(',')[1]
    return weather


def post_weathers_weatherdotcom(latitude, longitude):
    url = 'http://127.0.0.1:5000/weatherdotcom'
    data = {'lat': latitude, 'lon': longitude}
    headers = {'Content-Type': 'application/json'}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    weather_json = req.json()
    weather = {}
    weather['temperature'] = (int(weather_json['query']['results']['channel']['condition']['temp']))
    weather['service']="weatherdotcom"
    weather['latitude']=latitude
    weather['longitude']=longitude
    return weather
