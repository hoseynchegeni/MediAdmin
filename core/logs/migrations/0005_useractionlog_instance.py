# Generated by Django 4.2.11 on 2024-03-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logs", "0004_useractionlog"),
    ]

    operations = [
        migrations.AddField(
            model_name="useractionlog",
            name="instance",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
