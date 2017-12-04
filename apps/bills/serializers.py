from rest_framework import serializers

from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    bill = serializers.ReadOnlyField(source='branch')

    class Meta:
        model = Bill
        fields = ('id', 'debit', 'due_date', 'payment_date', 'bill', 'branch')
        # read_only_fields = ('slug', 'name', 'channel')

