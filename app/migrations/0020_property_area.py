# Generated by Django 5.0.7 on 2024-10-19 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_carport_spaces_property_car_port_spaces_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]