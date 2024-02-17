# Generated by Django 4.2.10 on 2024-02-17 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Consumable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("unit", models.CharField(max_length=50)),
                ("minimum_stock_level", models.PositiveIntegerField(default=0)),
                ("supplier", models.CharField(max_length=255)),
                ("purchase_date", models.DateField()),
                ("purchase_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("expiration_date", models.DateField(blank=True, null=True)),
                ("usage_notes", models.TextField(blank=True)),
                ("last_usage_date", models.DateField(blank=True, null=True)),
                ("location", models.CharField(max_length=255)),
                ("storage_notes", models.TextField(blank=True)),
                (
                    "depreciation_rate",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="in percentage",
                        max_digits=5,
                        null=True,
                    ),
                ),
                ("disposal_method", models.CharField(blank=True, max_length=100)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
