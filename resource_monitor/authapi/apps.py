from django.apps import AppConfig


class AuthapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authapi'
    
    def ready(self):
        # Ensure your signals are imported
        import authapi.signals