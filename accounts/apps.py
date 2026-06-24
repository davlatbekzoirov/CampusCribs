from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self):
        from . import signals  # Import signals when app is ready
