from rest_framework import serializers

from .models import Bill, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('slug', 'payment_date', 'bill')
        read_only_fields = ('slug', )


class BillSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True, source='payments')

    class Meta:
        model = Bill
        fields = ('slug', 'description', 'debit', 'due_date', 'branch', 'payment')
        read_only_fields = ('slug', 'payment')

