# Generated by Django 4.2.10 on 2024-03-10 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0008_client_number_of_reception"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="number_of_reception",
            new_name="number_of_receptions",
        ),
    ]
