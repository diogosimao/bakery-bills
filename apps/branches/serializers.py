from rest_framework import serializers

from .models import Branch


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('slug', 'description', 'address', 'city', 'state')
        read_only_fields = ('slug',)

