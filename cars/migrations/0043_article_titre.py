# Generated by Django 4.0.1 on 2022-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0042_remove_article_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Titre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
