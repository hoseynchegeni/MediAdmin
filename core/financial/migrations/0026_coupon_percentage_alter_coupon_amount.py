# Generated by Django 4.2.10 on 2024-03-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0025_financial_coupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="coupon",
            name="percentage",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="coupon",
            name="amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]