# Generated by Django 3.2.7 on 2021-09-26 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_auto_20210926_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_category',
            name='unlimited_kms_price',
        ),
        migrations.DeleteModel(
            name='Illimited_kms',
        ),
    ]
