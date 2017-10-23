from rest_framework.serializers import ModelSerializer
from .models import MonthlyReport, CashAndBackupAccount, InvestmentAccount, InsuranceAccount, Income, Outgoing


class CashAndBackupAccountSerializer(ModelSerializer):
    class Meta:
        model = CashAndBackupAccount
        exclude = ('month',)


class InvestmentAccountSerializer(ModelSerializer):
    class Meta:
        model = InvestmentAccount
        exclude = ('month',)


class InsuranceAccountSerializer(ModelSerializer):
    class Meta:
        model = InsuranceAccount
        exclude = ('month',)


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        exclude = ('month',)


class OutgoingSerializer(ModelSerializer):
    class Meta:
        model = Outgoing
        exclude = ('month', )


class MonthlyReportSerializer(ModelSerializer):
    cashes = CashAndBackupAccountSerializer(many=True)
    investments = InvestmentAccountSerializer(many=True)
    insurances = InsuranceAccountSerializer(many=True)
    incomes = IncomeSerializer(many=True)
    outgoings = OutgoingSerializer(many=True)

    class Meta:
        model = MonthlyReport
        fields = ('id', 'date', 'comments', 'investments', 'cashes', 'insurances', 'incomes', 'outgoings')

    def create(self, validated_data):
        cashes = validated_data.pop('cashes')
        investments = validated_data.pop('investments')
        insurances = validated_data.pop('insurances')
        incomes = validated_data.pop('incomes')
        outgoings = validated_data.pop('outgoings')

        month = MonthlyReport.objects.create(**validated_data)
        for cash in cashes:
            CashAndBackupAccount.objects.create(month=month, **cash)
        for investment in investments:
            InvestmentAccount.objects.create(month=month, **investment)
        for insurance in insurances:
            InsuranceAccount.objects.create(month=month, **insurance)
        for income in incomes:
            Income.objects.create(month=month, **income)
        for outgoing in outgoings:
            Outgoing.objects.create(month=month, **outgoing)
        return month
