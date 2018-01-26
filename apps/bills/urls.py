from django.conf.urls import include, url
from django.views import generic

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers

from .views import BillViewSet, PaymentViewSet, BillsCRUDFormView, BillCreate

router = DefaultRouter(trailing_slash=True)
router.register(r'bills_api', BillViewSet, base_name='bills_api')

bills_router = routers.NestedSimpleRouter(router, r'bills_api', lookup='bill')
bills_router.register(r'payment', PaymentViewSet, base_name='bill_api-payment')

schema_view = get_schema_view(title='Bakery bills API')

bills_patterns = ([
                      url('', include(BillsCRUDFormView().urls)),
                    ], '')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^$', generic.RedirectView.as_view(url='bills_crud/'), name="index"),
    url(r'^bills_crud/', include(bills_patterns)),
    url(r'^bills_custom/', BillCreate.as_view(), name='bills_custom'),
    url(r'^', include(bills_router.urls)),
    url(r'^', include(router.urls)),
]

