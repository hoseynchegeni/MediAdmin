# Generated by Django 4.2.10 on 2024-03-17 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "financial",
            "0015_officeexpenses_created_at_officeexpenses_created_by_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="officeexpenses",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="officeexpenses",
            name="is_approved",
        ),
    ]