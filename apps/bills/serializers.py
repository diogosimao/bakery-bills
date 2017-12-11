from rest_framework import serializers

from .models import Bill, Payment


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('slug', 'description', 'debit', 'due_date', 'branch')
        read_only_fields = ('slug', )


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('slug', 'payment_date')
        read_only_fields = ('slug', 'bill')

