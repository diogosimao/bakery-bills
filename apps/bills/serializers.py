from rest_framework import serializers

from .models import Bill, Payment


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('description', 'debit', 'due_date', 'branch')
        read_only_fields = ('slug', 'name')


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('slug', 'payment_date', 'bill')
        read_only_field = ('slug', )

