from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',  views.home_weather),
    path('<str:city_name>/<int:option>',views.home_weather_prediction)
]