from django.contrib.auth import get_user_model
from django.db import models

from recipeSharingApp.common.mixins import CreatedMixin, UpdatedMixin

UserModel = get_user_model()


class Tag(models.Model):
    TAG_MAX_LENGTH = 20

    name = models.CharField(
        max_length=TAG_MAX_LENGTH,
        unique=True,
    )

    def __str__(self):
        return self.name


class Like(models.Model):
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='likes',
    )

    recipe = models.ForeignKey(
        to='recipes.Recipe',
        on_delete=models.CASCADE,
        related_name='likes',
    )


class Comment(CreatedMixin, UpdatedMixin):
    content = models.TextField()

    recipe = models.ForeignKey(
        to='recipes.Recipe',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ['created_at']
