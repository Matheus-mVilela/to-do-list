from django.db import models
from . import choices
from uuid import uuid4

from django.db.models.base import Model

class Chore(models.Model):
    id_chore = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=choices.STATUS_CHOICES,
        null=False,
        blank=False,
        default=choices.STATUS_START,
    )


