from django.db import models


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class UpdatedMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
