# Generated by Django 4.2.10 on 2024-03-22 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0027_service_doctor_wage_percentage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="doctor_wage_percentage",
            new_name="doctors_wage_percentage",
        ),
    ]
