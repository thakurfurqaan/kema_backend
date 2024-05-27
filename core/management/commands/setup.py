from django.core.management.base import BaseCommand
from django.db import transaction

from merchants.models import Merchant
from payments.models import Currency

merchants = [
    {"business_name": "Google", "email": "google@google.com"},
    {"business_name": "Microsoft", "email": "microsoft@microsoft.com"},
    {"business_name": "Apple", "email": "apple@apple.com"},
    {"business_name": "Amazon", "email": "amazon@amazon.com"},
]

currencies = [
    {"name": "US Dollar", "code": "USD"},
    {"name": "Euro", "code": "EUR"},
    {"name": "Pound Sterling", "code": "GBP"},
]


class Command(BaseCommand):
    help = "Do the initial setup for the project to run."

    def handle(self, *args, **options):

        # Upload Merchant data
        with transaction.atomic():
            for merchant in merchants:
                merchant, created = Merchant.objects.update_or_create(**merchant)
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Successfully created Merchant {merchant}")
                    )

        # Upload Currency data
        with transaction.atomic():
            for currency in currencies:
                currency, created = Currency.objects.update_or_create(**currency)
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Successfully created Currency {currency}")
                    )

        self.stdout.write(self.style.SUCCESS("Successfully uploaded data."))
