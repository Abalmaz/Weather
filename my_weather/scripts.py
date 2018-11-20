import random

from django.utils import timezone

from my_weather.models import Weather, Source


def setup_weather_for_source(source_id):
    try:
        source = Source.objects.filter(id=source_id).first()
        if source:
            if source.is_update:
                source.set_status(Source.RUNNING)
                today = timezone.localdate()
                temperature = random.randint(-10, 10)
                setup_weather_for_source(source)
                Weather.objects.update_or_create(source=source,
                                                 date=today,
                                                 defaults={
                                                     'temperature': temperature}
                                                 )
                source.set_status(source.DONE)
            else:
                raise ValueError("Can't update weather for this source")
    except (ValueError, Exception):
        return


