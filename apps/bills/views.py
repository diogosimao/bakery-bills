import json

from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from material.frontend.views import ModelViewSet
from material import LayoutMixin, Layout, Row
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status

from .forms import BillForm, PaymentForm
from .models import Bill, Payment
from .serializers import BillSerializer, PaymentSerializer


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter_ = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter_[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter_)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


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

    def create(self, request, *args, **kwargs):
        response = super(BillViewSet, self).create(request, *args, **kwargs)
        messages.success(request, 'Bill added!')
        return HttpResponseRedirect(redirect_to=reverse_lazy('bills:bills_custom'))


class PaymentViewSet(MultipleFieldLookupMixin,
                     viewsets.ModelViewSet):
    """
    retrieve:
    Return the given payment.

    list:
    Return a list of all the existing payments.

    create:
    Create a new payment instance.
    """
    lookup_fields = ('bill_slug',)
    lookup_field = 'slug'
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        data = kwargs
        data.update(request.data.dict())
        data['bill'] = data.pop('bill_slug')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        messages.success(request, 'Payment registered!')
        return Response(json.dumps({'msg': str(reverse_lazy('bills:payments_custom'))}),
                        status=status.HTTP_201_CREATED, headers=headers, content_type="application/json")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        if args or kwargs:
            instance = self.get_object()
        else:
            instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BillsCRUDFormView(LayoutMixin, ModelViewSet):
    model = Bill
    layout = Layout(
            Row('description', 'debit', 'due_date', 'branch'),
        )


class BillCreate(FormView):
    template_name = 'create_form.html'
    model = Bill
    form_class = BillForm
    form_action = reverse_lazy('bills_api:bills_api-list')

    def get_context_data(self, **kwargs):
        context = super(BillCreate, self).get_context_data(**kwargs)
        context['form_action'] = self.form_action
        return context


class PaymentsCRUDFormView(LayoutMixin, ModelViewSet):
    model = Payment
    layout = Layout(
            Row('payment_date', 'bill'),
        )


class PaymentCreate(FormView):
    template_name = 'bills/payments_create_form.html'
    model = Payment
    form_class = PaymentForm
    form_action = reverse_lazy('bills_api:bill_api-payment-list', kwargs={'bill_slug': 'bill_slug'})

    def get_context_data(self, **kwargs):
        context = super(PaymentCreate, self).get_context_data(**kwargs)
        context['form_action'] = self.form_action
        return context

