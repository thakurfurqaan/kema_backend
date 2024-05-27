from rest_framework import serializers

from merchants.serializers import MerchantSerializer

from .models import Currency, PaymentRequest, Transaction


class PaymentRequestSerializer(serializers.ModelSerializer):
    merchant_details = MerchantSerializer(source="merchant", read_only=True)
    currency_code = serializers.CharField(source="currency.code", read_only=True)

    class Meta:
        model = PaymentRequest
        fields = [
            "id",
            "merchant",
            "amount",
            "currency",
            "status",
            "created_at",
            "merchant_details",
            "currency_code",
            "customer_email",
            "customer_card_number",
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "payment", "status", "created_at"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "code"]
