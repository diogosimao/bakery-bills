from django.contrib import admin

from .models import Bill, Payment


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    exclude = ('slug',)
