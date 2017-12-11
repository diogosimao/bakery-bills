from rest_framework.response import Response

from .models import Bill, Payment
from .serializers import BillSerializer, PaymentSerializer
from rest_framework import viewsets


class BillViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given bill.

    list:
    Return a list of all the existing bills.

    create:
    Create a new bill instance.
    """
    lookup_field = 'slug'
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given payment.

    list:
    Return a list of all the existing payments.

    create:
    Create a new payment instance.
    """
    lookup_field = 'slug'
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

