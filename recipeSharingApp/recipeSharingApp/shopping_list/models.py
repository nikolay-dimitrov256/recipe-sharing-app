from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ShoppingList(models.Model):
    products = models.JSONField(
        default=dict
    )

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )
