from django.contrib.auth import get_user_model
from django.db import models

from recipeSharingApp.common.mixins import CreatedMixin, UpdatedMixin

UserModel = get_user_model()


class Recipe(CreatedMixin, UpdatedMixin):
    title = models.CharField(
        max_length=150,
    )

    ingredients = models.JSONField(
        default=dict,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    instructions = models.TextField()

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
    )

    tags = models.ManyToManyField(
        to='common.Tag',
        related_name='tagged_recipes',
        blank=True,
    )

