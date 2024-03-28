# Generated by Django 4.2.11 on 2024-03-27 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0029_alter_service_doctors_wage_percentage"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceSpecification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("attribute_key", models.CharField(max_length=100)),
                ("attribute_value", models.CharField(max_length=500)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="services.service",
                    ),
                ),
            ],
        ),
    ]