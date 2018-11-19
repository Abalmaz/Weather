from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=25)
    is_update = models.BooleanField(default=True)
    status = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Weather(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.IntegerField()
