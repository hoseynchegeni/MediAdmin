# Generated by Django 4.2.10 on 2024-02-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
