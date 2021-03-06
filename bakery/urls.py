"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

from django.conf.urls import include, url
from django.shortcuts import render
from rest_framework.documentation import include_docs_urls
from material.frontend import urls as frontend_urls

bills_patterns = ([
                          url('', include('apps.bills.urls')),
                      ], 'bills_api')

branches_patterns = ([
                             url('', include('apps.branches.urls')),
                         ], 'branches_api')

material_patterns = ([
                        url('', include(frontend_urls)),
                     ], '')


def index_view(request):
    return render(request, 'index.html')


urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^docs/', include_docs_urls(title='Bakery bills API Documentation', public=False)),
    url(r'', include(material_patterns)),
    url(r'^api/', include(bills_patterns)),
    url(r'^api/', include(branches_patterns)),
    url(r'^$', index_view, name='index'),
]

