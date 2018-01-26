from django.conf.urls import include, url
from django.views import generic
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import BranchViewSet, BranchesCRUDFormView, BranchCreate

router = DefaultRouter(trailing_slash=True)
router.register(r'branches_api', BranchViewSet, base_name='branches_api')

schema_view = get_schema_view(title='Bakery branches API')

branches_patterns = ([
                         url('', include(BranchesCRUDFormView().urls)),
                     ], '')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^$', generic.RedirectView.as_view(url='branches_crud/'), name="index"),
    url(r'^branches_crud/', include(branches_patterns)),
    url(r'^branches_custom/', BranchCreate.as_view(), name='branches_custom'),
    url(r'^', include(router.urls)),
]

