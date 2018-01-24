from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class BillsConfig(ModuleMixin, AppConfig):
    name = 'apps.bills'
