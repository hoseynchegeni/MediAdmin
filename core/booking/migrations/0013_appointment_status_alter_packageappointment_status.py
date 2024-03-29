# Generated by Django 4.2.10 on 2024-03-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0012_packageappointment_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("WAITE", "WAITE"), ("DONE", "DONE")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="packageappointment",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("WAITE", "WAITE"), ("DONE", "DONE")],
                max_length=100,
                null=True,
            ),
        ),
    ]
