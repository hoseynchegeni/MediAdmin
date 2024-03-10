# Generated by Django 4.2.10 on 2024-03-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0007_service_off_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="off_day",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Sunday"),
                    (1, "Monday"),
                    (2, "Tuesday"),
                    (3, "Wednesday"),
                    (4, "Thursday"),
                    (5, "Friday"),
                    (6, "Saturday"),
                ],
                default=4,
            ),
        ),
    ]