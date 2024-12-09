from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipeSharingApp.accounts'

    def ready(self):
        import recipeSharingApp.accounts.signals
