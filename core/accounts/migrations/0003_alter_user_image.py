# Generated by Django 4.2.10 on 2024-03-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_address_alter_user_date_of_birth_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, default="images/default.png", null=True, upload_to="images"
            ),
        ),
    ]