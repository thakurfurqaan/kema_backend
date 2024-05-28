from rest_framework import viewsets

from .models import Merchant
from .serializers import MerchantSerializer


class MerchantViewSet(viewsets.ModelViewSet):
    # Would normally require a permission class: IsAuthenticated with other custom permissions.

    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
