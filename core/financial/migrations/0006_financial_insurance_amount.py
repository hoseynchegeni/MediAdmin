# Generated by Django 4.2.10 on 2024-02-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0005_financial_insurance_range"),
    ]

    operations = [
        migrations.AddField(
            model_name="financial",
            name="insurance_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]