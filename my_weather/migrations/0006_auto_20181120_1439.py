# Generated by Django 2.1.3 on 2018-11-20 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_weather', '0005_auto_20181120_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Running'), (2, 'Done'), (3, 'Error')]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weathers', to='my_weather.Source'),
        ),
    ]
