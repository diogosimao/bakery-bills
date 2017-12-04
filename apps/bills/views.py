from .models import Bill
from .serializers import BillSerializer
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

    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def perform_create(self, serializer):
        serializer.save(branch_id=self.request.branch.id)

