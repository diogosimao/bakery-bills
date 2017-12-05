from rest_framework import viewsets

from .models import Branch
from .serializers import BranchSerializer


class BranchViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given branch.

    list:
    Return a list of all the existing branches.

    create:
    Create a new branch instance.
    """

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

