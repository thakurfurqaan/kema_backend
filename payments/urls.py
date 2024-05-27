from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CurrencyViewSet, PaymentRequestViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r"requests", PaymentRequestViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"currencies", CurrencyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
