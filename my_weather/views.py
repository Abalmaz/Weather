from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

from django.views.generic.list import ListView

from my_weather.tasks import setup_weather_for_source
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


def update_source(request):
    if request.method == 'POST' and request.is_ajax():
        data = request.POST
        source = get_object_or_404(Source, pk=data['pk'])
        source.is_update = not source.is_update
        source.save()
        return JsonResponse({'status': 'success'})


def update_weather_for_source(request):
    if request.method == 'POST' and request.is_ajax():
        status = 'failed'
        data = request.POST
        source = get_object_or_404(Source, pk=data['pk'])
        if source.is_update:
            setup_weather_for_source(source)
            status = 'success'
        return JsonResponse({'status': status})


