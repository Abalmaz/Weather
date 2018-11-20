from celery import shared_task

from my_weather.models import Source
from my_weather.scripts import run_update_weather


@shared_task
def run_update_weather_for_all_source():
    sources = Source.objects.all()
    for source in sources:
        run_update_weather(source.id)


