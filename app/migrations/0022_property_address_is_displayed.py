# Generated by Django 5.0.7 on 2024-10-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_area_property_mls_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address_is_displayed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]