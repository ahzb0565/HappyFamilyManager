from rest_framework import serializers
from .models.Fund import Fund


class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ('id', 'name', 'fund_id', 'company', 'type')
