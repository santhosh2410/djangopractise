from django.apps import AppConfig


class AccountDetailsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "account_details"

    def ready(self):
        import account_details.signals
