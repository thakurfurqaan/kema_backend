from django.contrib import admin

from payments.models import Currency, PaymentRequest, Transaction

admin.site.register([Currency, PaymentRequest, Transaction])
