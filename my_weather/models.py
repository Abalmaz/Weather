from django.db import models


class Source(models.Model):
    RUNNING = 1
    DONE = 2
    ERROR = 3
    STATUSES = (
        (RUNNING, 'Running'),
        (DONE, 'Done'),
        (ERROR, 'Error'),
    )

    name = models.CharField(max_length=25)
    is_update = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField(choices=STATUSES, blank=True)
    url = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def set_status(self, status):
        if status in dict(self.STATUSES):
            self.status = status
            self.save()


class Weather(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE,
                               related_name='weathers')
    date = models.DateField()
    temperature = models.IntegerField()

    class Meta:
        ordering = ('-date',)
        unique_together = (("source", "date"),)
