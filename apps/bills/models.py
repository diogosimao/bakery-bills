from django.db import models

from bakery.core.models import DefaultBaseModel
from apps.branches.models import Branch


class CustomOneToOneField(models.OneToOneField):
    def get_attname(self):
        return '%s_slug' % self.name


class CustomForeignKey(models.ForeignKey):
    def get_attname(self):
        return '%s_slug' % self.name


class Bill(DefaultBaseModel):
    description = models.CharField(max_length=255, blank=False, null=False)
    debit = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    branch = CustomForeignKey(Branch, related_name='bills', on_delete=models.CASCADE, to_field='slug',
                              db_column='branch_slug', verbose_name='branch_slug')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('due_date',)
        verbose_name_plural = 'bills'


class Payment(DefaultBaseModel):
    payment_date = models.DateField(blank=False, null=False)
    bill = CustomOneToOneField(Bill, related_name='payments', on_delete=models.CASCADE, to_field='slug',
                               db_column='bill_slug')

    def __str__(self):
        return '{}'.format(self.payment_date)

    class Meta:
        ordering = ('payment_date',)
        verbose_name_plural = 'payments'

