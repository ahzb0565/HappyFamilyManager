from rest_framework.serializers import ModelSerializer
from .models import CashAndBackupAccount


class CashAndBackupAccountSerializer(ModelSerializer):
    class Meta:
        model = CashAndBackupAccount
        fields = '__all__'
