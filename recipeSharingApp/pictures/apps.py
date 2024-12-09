from django.apps import AppConfig


class PicturesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipeSharingApp.pictures'

    def ready(self):
        import recipeSharingApp.pictures.signals
