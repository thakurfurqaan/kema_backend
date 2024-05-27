import uuid

from django.db import models

from kema_backend import settings


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    deleted = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
