from django.db import models

from bakery.core.models import DefaultBaseModel


class Branch(DefaultBaseModel):
    address = models.CharField(unique=True, max_length=200, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('address',)
        verbose_name_plural = 'branches'

