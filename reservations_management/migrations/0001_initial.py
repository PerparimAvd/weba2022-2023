# Generated by Django 3.2.7 on 2021-09-24 18:16

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 24, 18, 16, 26, 969996, tzinfo=utc), null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('date_location_start', models.DateTimeField(blank=True, null=True)),
                ('date_location_end', models.DateTimeField(blank=True, null=True)),
                ('hoursDriving', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('kms', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('car_price', models.IntegerField(blank=True, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.car')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
            ],
        ),
    ]
