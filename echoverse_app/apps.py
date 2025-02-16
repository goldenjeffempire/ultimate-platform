from django.apps import AppConfig


class EchoverseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'echoverse_app'

    def ready(self):
        import echoverse_app.signals
