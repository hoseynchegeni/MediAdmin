# Generated by Django 4.2.10 on 2024-03-14 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0015_remove_service_equipment_supplies_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="availability",
        ),
    ]
