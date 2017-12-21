from rest_framework.serializers import ModelSerializer
from .models import Item, MonthReport


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class MonthReportSerializer(ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = MonthReport
        fields = '__all__'
        read_only_fields = ('total', 'income', 'outcome')