from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.views.generic.list import ListView

from .models import Weather


class WeatherListView(ListView):
    model = Weather
    template_name = 'my_weather/show_weather.html'
    context_object_name = 'temperatures'
    today = timezone.now() - timedelta(days=5)
    queryset = Weather.objects.filter(date__gt=today).order_by('-date')
