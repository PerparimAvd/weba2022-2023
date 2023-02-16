# Generated by Django 3.2.7 on 2021-09-28 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0024_auto_20210928_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price_categories',
            field=models.ManyToManyField(through='cars.Price', to='cars.Price_category'),
        ),
        migrations.AlterField(
            model_name='price',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AlterField(
            model_name='price',
            name='car_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='price',
            name='price_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.price_category'),
        ),
    ]