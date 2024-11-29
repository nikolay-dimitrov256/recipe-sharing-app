from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from recipeSharingApp.accounts.models import Profile
from recipeSharingApp.pictures.models import Gallery

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance: UserModel, created: bool, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_gallery(sender, instance: Profile, created: bool, **kwargs):
    if created and not hasattr(instance, 'gallery'):
        Gallery.objects.create(profile=instance)
