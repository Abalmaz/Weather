import random

from django.utils import timezone

from my_weather.models import Weather, Source


def setup_weather_for_source(source):
    source.set_status(Source.RUNNING)
    today = timezone.localdate()
    temperature = random.randint(-10, 10)
    Weather.objects.update_or_create(source=source,
                                     date=today,
                                     defaults={
                                         'temperature': temperature}
                                     )
    source.set_status(Source.DONE)

