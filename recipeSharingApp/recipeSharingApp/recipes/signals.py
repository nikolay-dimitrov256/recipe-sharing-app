from django.db.models.signals import post_save
from django.dispatch import receiver

from recipeSharingApp.pictures.models import Gallery
from recipeSharingApp.recipes.models import Recipe


@receiver(post_save, sender=Recipe)
def create_recipe_gallery(sender, instance: Recipe, created: bool, **kwargs):
    if created:
        Gallery.objects.create(recipe=instance)
