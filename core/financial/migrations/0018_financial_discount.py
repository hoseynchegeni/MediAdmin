# Generated by Django 4.2.10 on 2024-03-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0017_financial_tax"),
    ]

    operations = [
        migrations.AddField(
            model_name="financial",
            name="discount",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
