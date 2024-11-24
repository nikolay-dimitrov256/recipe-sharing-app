from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=20,
    )


class Like(models.Model):
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        to='recipes.Recipe',
        on_delete=models.CASCADE,
    )
