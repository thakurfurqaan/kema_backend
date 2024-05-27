from django.db import models

from core.models import BaseModel


class Merchant(BaseModel):
    business_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.business_name
