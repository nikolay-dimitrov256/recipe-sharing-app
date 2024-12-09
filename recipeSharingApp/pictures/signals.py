from cloudinary import uploader
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from recipeSharingApp.pictures.models import Picture


@receiver(pre_delete, sender=Picture)
def delete_picture_from_cloudinary(sender, instance: Picture, **kwargs):
    if instance:
        public_id = instance.image.public_id

        if public_id:
            uploader.destroy(public_id)
