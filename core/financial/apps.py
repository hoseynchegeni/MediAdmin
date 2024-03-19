from django.apps import AppConfig


class FinancialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "financial"

    def ready(self):
        # Import the signal handler function
        from .signals import create_financial, generate_coupon_code
