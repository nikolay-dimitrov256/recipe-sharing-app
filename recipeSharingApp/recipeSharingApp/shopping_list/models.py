from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ShoppingList(models.Model):
    products = models.JSONField(
        default=dict,
        blank=True,
    )

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user.full_name}\'s shopping list'
