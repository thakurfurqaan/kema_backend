import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    MERCHANT = "MERCHANT", "Merchant"
    CUSTOMER = "CUSTOMER", "Customer"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=255,
        choices=Role.choices,
        default=Role.MERCHANT,
    )

    allow_notifications = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    @property
    def is_merchant(self):
        return self.role == Role.MERCHANT

    @property
    def is_customer(self):
        return self.role == Role.CUSTOMER
