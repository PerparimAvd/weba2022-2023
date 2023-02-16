# Generated by Django 3.2.7 on 2021-10-14 20:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0044_auto_20211014_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_location_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time_location_start',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
