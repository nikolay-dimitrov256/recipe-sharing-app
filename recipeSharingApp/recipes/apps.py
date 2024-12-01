from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipeSharingApp.recipes'

    def ready(self):
        import recipeSharingApp.recipes.signals
