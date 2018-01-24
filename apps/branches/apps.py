from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class BranchesConfig(ModuleMixin, AppConfig):
    name = 'apps.branches'
