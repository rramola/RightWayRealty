# Generated by Django 5.0.7 on 2024-10-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_navicaproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='baths_total',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
