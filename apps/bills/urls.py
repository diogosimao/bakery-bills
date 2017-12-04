from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import BillViewSet


router = DefaultRouter()
router.register(r'', BillViewSet, base_name='bills')


schema_view = get_schema_view(title='Bakery bills API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]

