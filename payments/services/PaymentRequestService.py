from payments.models import PaymentRequest


class PaymentRequestService:
    def __init__(self, payment_request: PaymentRequest = None):
        self.payment_request = payment_request

    def create_payment_request(self, merchant_id: str, amount: str, currency: str):
        pr = PaymentRequest.objects.create(
            merchant_id=merchant_id, amount=amount, currency=currency
        )
        self.payment_request = pr
        return pr
