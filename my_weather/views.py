from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Weather


class WeatherListView(ListView):
    model = Weather
    template_name = 'my_weather/show_weather.html'
