# Generated by Django 4.2.10 on 2024-03-04 13:34

import booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0007_alter_appointment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="date",
            field=models.DateField(
                validators=[booking.models.validate_max_appointments_per_day]
            ),
        ),
    ]
