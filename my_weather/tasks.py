from my_weather.models import Source
from my_weather.scripts import setup_weather_for_source, \
    change_status_for_source


def run_update_weather(source_id):
    try:
        source = Source.objects.filter(id=source_id).first()
        if source:
            if source.is_update:
                change_status_for_source(source.id, "Running")
                setup_weather_for_source(source)
                change_status_for_source(source.id, "Done")
            else:
                raise ValueError("Can't update weather for this source")
    except (ValueError, Exception) as e:
        return False, e

