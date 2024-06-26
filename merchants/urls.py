from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MerchantViewSet

router = DefaultRouter()
router.register(r"", MerchantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
