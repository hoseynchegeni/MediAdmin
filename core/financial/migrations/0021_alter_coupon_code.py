# Generated by Django 4.2.10 on 2024-03-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0020_remove_coupon_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coupon",
            name="code",
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
