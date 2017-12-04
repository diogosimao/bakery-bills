from django.db import models
from bakery.core.models import TimestampedModel


class Branch(TimestampedModel):
    address = models.CharField(unique=True, max_length=200, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ('address',)
        verbose_name_plural = "branches"

