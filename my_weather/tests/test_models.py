from django.db import IntegrityError
from django.test import TestCase

from my_weather.models import Source, Weather


class SourceModelTest(TestCase):
    def setUp(self):
        self.source = Source.objects.create(name='test_source',
                                            url='test_source.com',
                                            status=2)

    def test_name_max_length(self):
        max_length = self.source._meta.get_field('name').max_length
        self.assertEquals(max_length, 25)

    def test_url_max_length(self):
        max_length = self.source._meta.get_field('url').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        expected_object_name = '{}'.format(self.source.name)
        self.assertEquals(expected_object_name, str(self.source))

    def test_set_status_with_correct_value(self):
        self.source.set_status(Source.RUNNING)
        self.source.save()
        self.assertEquals('Running', self.source.get_status_display())

    def test_set_status_with_incorrect_value(self):
        self.source.set_status(4)
        self.assertNotEquals(4, self.source.status)


class WeatherModelTest(TestCase):
    def setUp(self):
        self.source = Source.objects.create(name='test_source',
                                            url='test_source.com',
                                            status=2)
        self.weather1 = Weather.objects.create(source=self.source,
                                               date='2018-11-18',
                                               temperature=2)

    def test_unique_date_for_source(self):
        with self.assertRaises(IntegrityError):
            Weather.objects.create(source=self.source,
                                   date='2018-11-18',
                                   temperature=3)


