import random

from django.utils import timezone

from my_weather.models import Weather, Source


def change_status_for_source(source_id, status):
    try:
        source = Source.objects.filter(id=source_id).first()
        if source:
            source.status = status
            source.save()
        else:
            raise ValueError('this source is not exist')
    except (ValueError, Exception) as e:
        return False, e


def setup_weather_for_source(source):
    today = timezone.localdate()
    temperature = random.randint(-10, 10)
    Weather.objects.update_or_create(source=source,
                                     date=today,
                                     temperature=temperature)
    change_status_for_source(source.id, "Done")


def run_update_weather(source_id):
    try:
        source = Source.objects.filter(id=source_id).first()
        if source:
            if source.is_update:
                change_status_for_source(source_id, "Running")
                setup_weather_for_source(source)
            else:
                raise ValueError("Can't update weather for this source")
    except (ValueError, Exception) as e:
        return


