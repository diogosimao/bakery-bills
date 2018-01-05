from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from .forms import BranchForm
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
    lookup_field = 'slug'
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def create(self, request, *args, **kwargs):
        response = super(BranchViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to=reverse_lazy('branches'))


class SubscribeView(generic.FormView):
    template_name = 'branches.html'
    form_class = BranchForm
    success_url = reverse_lazy('branches')

