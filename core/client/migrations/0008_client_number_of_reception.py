# Generated by Django 4.2.10 on 2024-03-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0007_alter_client_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="number_of_reception",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
