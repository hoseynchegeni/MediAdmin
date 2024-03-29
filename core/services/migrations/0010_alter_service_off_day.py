# Generated by Django 4.2.10 on 2024-03-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0009_alter_service_off_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="off_day",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Monday"),
                    (1, "Tuesday"),
                    (2, "Wednesday"),
                    (3, "Thursday"),
                    (4, "Friday"),
                    (5, "Saturday"),
                    (6, "Sunday"),
                ],
                default=6,
            ),
        ),
    ]
