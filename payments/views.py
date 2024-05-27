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

    # Payment API - Pay
    @action(detail=True, methods=["post"])
    def pay(self, request, pk=None):
        payment_request: PaymentRequest = self.get_object()
        if payment_request.status != PaymentRequest.StatusChoices.PENDING:
            return Response(
                {"status": "Payment already processed"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        card_number = request.data.get("cardNumber")
        email = request.data.get("email")

        if not card_number or not email:
            return Response(
                {"error": "Card number and email are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Save card details and email
        payment_request.customer_card_number = card_number
        payment_request.customer_email = email
        payment_request.status = PaymentRequest.StatusChoices.PAID
        payment_request.save()

        self._update_payment_request_status(
            payment_request, PaymentRequest.StatusChoices.PAID
        )
        self._create_completed_transaction(payment_request)
        return Response({"status": "Payment processed"}, status=status.HTTP_200_OK)

    # Payment API - Refund
    @action(detail=True, methods=["post"])
    def refund(self, request, pk=None):
        payment_request: PaymentRequest = self.get_object()
        if payment_request.status != PaymentRequest.StatusChoices.PAID:
            return Response(
                {"status": "Payment not processed yet"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Payment Gateway Refund logic
        self._update_payment_request_status(
            payment_request, PaymentRequest.StatusChoices.REFUNDED
        )
        return Response({"status": "Payment refunded"}, status=status.HTTP_200_OK)

    # Payment API - Status
    @action(detail=True, methods=["get"])
    def status(self, request, pk=None):
        payment_request: PaymentRequest = self.get_object()
        return Response({"status": payment_request.status}, status=status.HTTP_200_OK)

    def _create_completed_transaction(self, payment_request: PaymentRequest):
        return Transaction.objects.create(
            payment=payment_request, status=Transaction.StatusChoices.COMPLETED
        )

    def _update_payment_request_status(self, payment_request, status):
        payment_request.status = status
        payment_request.save()


class PaymentGatewayCallback(viewsets.ViewSet):
    @action(detail=False, methods=["post"])
    def callback(self, request):
        payment_request_id = request.data.get("payment_request_id")
        payment_request = PaymentRequest.objects.get(id=payment_request_id)
        payment_request.status = PaymentRequest.StatusChoices.PAID
        payment_request.save()
        return Response({"status": "Payment processed"}, status=status.HTTP_200_OK)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
