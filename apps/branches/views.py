from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from rest_framework import viewsets
from material.frontend.views import ModelViewSet

from apps.branches.forms import BranchForm
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
        messages.success(request, 'Branch added!')
        return HttpResponseRedirect(redirect_to=reverse_lazy('branches:branches_custom'))


class BranchesCRUDFormView(ModelViewSet):
    model = Branch


class BranchCreate(FormView):
    template_name = 'create_form.html'
    model = Branch
    form_class = BranchForm
    form_action = reverse_lazy('branches_api:branches_api-list')

    def get_context_data(self, **kwargs):
        context = super(BranchCreate, self).get_context_data(**kwargs)
        context['form_action'] = self.form_action
        return context
