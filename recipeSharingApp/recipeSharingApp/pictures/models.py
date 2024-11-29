from django.db import models
from cloudinary.models import CloudinaryField

from recipeSharingApp.pictures.managers import PictureManager


class Picture(models.Model):
    image = CloudinaryField('image')

    is_main = models.BooleanField(
        default=False,
        blank=True,
    )

    gallery = models.ForeignKey(
        to='Gallery',
        on_delete=models.CASCADE,
        related_name='pictures',
    )

    objects = PictureManager()

    def save(self, *args, **kwargs):

        if self.is_main:
            # Ensure no other picture in this gallery is main
            Picture.objects.filter(gallery=self.gallery, is_main=True).exclude(id=self.id).update(is_main=False)

        super().save(*args, **kwargs)


class Gallery(models.Model):
    profile = models.OneToOneField(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    recipe = models.OneToOneField(
        to='recipes.Recipe',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
