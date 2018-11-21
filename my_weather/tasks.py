from celery import shared_task

from my_weather.models import Source
from my_weather.scripts import setup_weather_for_source


@shared_task
def run_update_weather_for_all_source():
    sources = Source.objects.filter(is_update=True)
    for source in sources:
        setup_weather_for_source(source)
