from django.db import models
from bakery.core.models import TimestampedModel

from apps.branches.models import Branch


class Bill(TimestampedModel):
    debit = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    due_date = models.DateField(blank=False)
    payment_date = models.DateField(null=True, blank=True)
    branch = models.ForeignKey(Branch, related_name='bills', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(self.branch.name, self.debit, self.due_date)

    class Meta:
        ordering = ('due_date',)
        verbose_name_plural = "bills"

