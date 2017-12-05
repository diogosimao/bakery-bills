from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import BranchViewSet


router = DefaultRouter(trailing_slash=True)
router.register(r'branches', BranchViewSet, base_name='branches')

schema_view = get_schema_view(title='Bakery branches API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]