# Generated by Django 4.2.10 on 2024-02-24 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
        ("services", "0002_serviceconsumable"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="doctor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="doctor.doctor",
            ),
        ),
    ]
