from django.test import TestCase
from django.urls import reverse, resolve

from my_weather.models import Source
from my_weather.views import SourceListView


class SourceListViewTest(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_source_list_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_source_list_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'my_weather/show_weather.html')

    def test_home_url_resolves_source_list_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, SourceListView)


class UpdateSourceViewTest(TestCase):
    def setUp(self):
        self.source = Source.objects.create(name='test_source',
                                            url='test_source.com',
                                            status=2)
        self.response = self.client.post('/update_source/',
                                         {'pk': self.source.pk},
                                         HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                                         )

    def test_update_source_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_update_source_view_not_found_status_code(self):
        response = self.client.post('/update_source/',
                                    {'pk': 999999},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                                    )
        self.assertEquals(response.status_code, 404)


class UpdateWeatherForSourceViewTest(TestCase):
    def setUp(self):
        self.source = Source.objects.create(name='test_source',
                                            url='test_source.com',
                                            status=2)
        self.response = self.client.post('/update_weather/',
                                         {'pk': self.source.pk},
                                         HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                                         )

    def test_update_weather_for_source_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)
