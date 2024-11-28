from django.db import models
from cloudinary.models import CloudinaryField


class Picture(models.Model):
    image = CloudinaryField('image')

    class Meta:
        abstract = True


class ProfilePicture(Picture):
    profile = models.OneToOneField(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='profile_picture',
    )


class RecipePicture(Picture):
    recipe = models.ForeignKey(
        to='recipes.Recipe',
        on_delete=models.CASCADE,
        related_name='gallery',
    )

