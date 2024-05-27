from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Currency, PaymentRequest, Transaction
from .serializers import (
    CurrencySerializer,
    PaymentRequestSerializer,
    TransactionSerializer,
)


class PaymentRequestViewSet(viewsets.ModelViewSet):
    queryset = PaymentRequest.objects.all()
    serializer_class = PaymentRequestSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    @action(detail=True, methods=["post"])
    def process(self, request, pk=None):
        payment_request: PaymentRequest = self.get_object()
        payment_request.status = PaymentRequest.StatusChoices.PAID
        payment_request.save()
        self._create_transaction(payment_request)
        return Response({"status": "Payment processed"}, status=status.HTTP_200_OK)

    def _create_transaction(self, payment_request: PaymentRequest):
        return Transaction.objects.create(payment=payment_request, status="completed")


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
