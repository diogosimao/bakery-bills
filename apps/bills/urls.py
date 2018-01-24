from django.conf.urls import include, url
from django.views import generic

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers

from .views import BillViewSet, PaymentViewSet, BillsCRUDFormView
from .forms import BillForm

router = DefaultRouter(trailing_slash=True)
router.register(r'bills', BillViewSet, base_name='bills')

bills_router = routers.NestedSimpleRouter(router, r'bills', lookup='bill')
bills_router.register(r'payment', PaymentViewSet, base_name='bill-payment')

schema_view = get_schema_view(title='Bakery bills API')

bills_patterns = ([
                      url('', include(BillsCRUDFormView().urls)),
                    ], '')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^$', generic.RedirectView.as_view(url='bills_crud/'), name="index"),
    url(r'^bills_crud/', include(bills_patterns)),
    url(r'^bills_custom/$', generic.FormView.as_view(
        form_class=BillForm, success_url='/bills_custom/', template_name="bills.html")),
    url(r'^', include(router.urls)),
    url(r'^', include(bills_router.urls)),
]