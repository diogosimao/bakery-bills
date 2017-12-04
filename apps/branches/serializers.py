from rest_framework import serializers

from .models import Branch
from apps.bills.serializers import BillSerializer


class BranchSerializer(serializers.ModelSerializer):
    bills = BillSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = ('id', 'address', 'city', 'state', 'bills')
        read_only_fields = ('id',)

