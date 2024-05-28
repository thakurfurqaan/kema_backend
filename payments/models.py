from django.db import models

from core.models import BaseModel
from kema_backend import settings
from merchants.models import Merchant


class Currency(BaseModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PaymentRequest(BaseModel):
    """
    This model represents a payment request that has been made by a merchant.
    """

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    class StatusChoices(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PAID = "PAID", "Paid"
        CANCELLED = "CANCELLED", "Cancelled"
        REFUNDED = "REFUNDED", "Refunded"
        EXPIRED = "EXPIRED", "Expired"

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    customer_card_number = models.CharField(max_length=16, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)

    @property
    def payment_link(self):
        return f"{settings.FRONTEND_URL}/payment/{self.id}/"

    @property
    def qr_code(self):
        return f"https://api.qrserver.com/v1/create-qr-code/?data={self.payment_link}&size=200x200"


class Transaction(BaseModel):
    """
    This model represents a transaction that has been made for a payment request.
    It should contain the payment gateway details as well.
    """

    payment = models.ForeignKey(PaymentRequest, on_delete=models.CASCADE)

    class StatusChoices(models.TextChoices):
        CANCELLED = "CANCELLED", "Cancelled"
        REFUNDED = "REFUNDED", "Refunded"
        COMPLETED = "COMPLETED", "Completed"

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.COMPLETED,
    )
