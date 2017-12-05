from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers

from .views import BillViewSet, PaymentViewSet


router = DefaultRouter(trailing_slash=True)
router.register(r'bills', BillViewSet, base_name='bills')

bills_router = routers.NestedSimpleRouter(router, r'bills', lookup='bill', )
bills_router.register(r'payment', PaymentViewSet, base_name='bill-payment')


schema_view = get_schema_view(title='Bakery bills API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^', include(bills_router.urls)),
]

