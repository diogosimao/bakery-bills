from django.db import models
from bakery.core.models import TimestampedModel

from apps.branches.models import Branch


class Bill(TimestampedModel):
    description = models.CharField(max_length=255, blank=False, null=False)
    debit = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    branch = models.ForeignKey(Branch, related_name='bills', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('due_date',)
        verbose_name_plural = 'bills'


class Payment(models.Model):
    payment_date = models.DateField(blank=False, null=False)
    bill = models.OneToOneField(Bill, related_name='payments', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.payment_date)

    class Meta:
        ordering = ('payment_date',)
        verbose_name_plural = 'payments'

