from django.shortcuts import render
import requests
from datetime import datetime
from django.http import JsonResponse


# Create your views here.



def home_weather(request):
    #ovdje spremamo url od meteobaze
    url = 'http://meteo.pointjupiter.co/'
    response = requests.get(url.format()).json()
    # ovdje imamo spremljenu sad cijelu listu objekata gradova
    cities = response['cities']
    context = {
        'cities':cities
    }
    return JsonResponse(context)


def home_weather_prediction(request, city_name, option):
    now = datetime.now()
    curr_date = now.strftime("%Y-%m-%d")
    print(curr_date)
    url = 'http://meteo.pointjupiter.co/'
    response = requests.get(url.format()).json()
    cities = response['cities']
    weather_json = {
        'day_1':'',
        'day_2':'',
        'day_3':'',
        'day_4':'',
        'day_5':''
    }
    for city in cities:
        if city['name'] == city_name:
            if option == 1:
                city_url = city['url']
                responsee = requests.get(city_url.format()).json()
                weather_json={
                    'day_1':responsee['data'][0]['forecast']
                }
            if option == 3:
                city_url = city['url']
                responsee = requests.get(city_url.format()).json()
                weather_json = {
                    'day_1':responsee['data'][0]['forecast'],
                    'day_2':responsee['data'][1]['forecast'],
                    'day_3':responsee['data'][2]['forecast']
                }
            if option == 5:
                city_url=city['url']
                responsee = requests.get(city_url.format()).json()
                weather_json = {
                    'day_1':responsee['data'][0]['forecast'],
                    'day_2':responsee['data'][1]['forecast'],
                    'day_3':responsee['data'][2]['forecast'],
                    'day_4':responsee['data'][3]['forecast'],
                    'day_5':responsee['data'][4]['forecast']
                }

    return JsonResponse(weather_json)