# Generated by Django 4.2.10 on 2024-03-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0022_remove_servicepackage_gap_with_previous_service_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="preparation_instructions",
            field=models.TextField(blank=True, null=True),
        ),
    ]
