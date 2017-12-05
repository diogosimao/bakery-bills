from rest_framework import serializers

from .models import Bill, Payment


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('description', 'debit', 'due_date', 'branch')


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('payment_date', 'bill')

