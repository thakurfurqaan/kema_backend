from rest_framework import serializers

from .models import Currency, PaymentRequest, Transaction


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ["id", "merchant", "amount", "currency", "status", "created_at"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "payment", "status", "created_at"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "code"]
