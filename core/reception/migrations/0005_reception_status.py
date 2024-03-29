# Generated by Django 4.2.10 on 2024-02-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reception", "0004_reception_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="reception",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("WAITE", "Waite"), ("DONE", "Done")],
                max_length=10,
                null=True,
            ),
        ),
    ]
