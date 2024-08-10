# Generated by Django 5.0.7 on 2024-08-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_alter_property_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="private_remarks",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="public_remarks",
            field=models.TextField(blank=True, null=True),
        ),
    ]
