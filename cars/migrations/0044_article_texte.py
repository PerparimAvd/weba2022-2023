# Generated by Django 4.0.1 on 2022-01-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0043_article_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Texte',
            field=models.TextField(null=True),
        ),
    ]
