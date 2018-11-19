from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.views.generic.list import ListView

from .models import Source


class SourceListView(ListView):
    model = Source
    template_name = 'my_weather/show_weather.html'
    context_object_name = 'sources'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        today = timezone.localdate()
        min_date = today - timedelta(days=5)
        context['min_date'] = min_date

        return context

