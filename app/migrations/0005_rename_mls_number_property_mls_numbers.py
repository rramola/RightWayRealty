# Generated by Django 5.0.7 on 2024-10-20 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_property_modification_timestamp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='mls_number',
            new_name='mls_numbers',
        ),
    ]
