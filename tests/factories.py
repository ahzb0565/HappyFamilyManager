import factory
from api.models import MonthlyReport, CashAndBackupAccount, InvestmentAccount, InsuranceAccount, Income, Outgoing
from api.constants import INSURANCE_TYPE
from datetime import datetime, timedelta
import random


class MonthlyReportFactory(factory.DjangoModelFactory):
    class Meta:
        model = MonthlyReport
    comments = factory.sequence(lambda n: 'comments {}'.format(n))
    date = datetime.today()


class CashAndBackupAccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = CashAndBackupAccount

    month = factory.SubFactory(MonthlyReport)
    name = factory.sequence(lambda n: 'cash {}'.format(n))
    money = random.uniform(1, 1000)
    comments = 'cash comments'


class InvestmentAccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = InvestmentAccount

    month = factory.SubFactory(MonthlyReport)
    name = factory.sequence(lambda n: 'investment {}'.format(n))
    money = random.uniform(1, 1000)
    comments = 'investment comments'


class InsuranceAccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = InsuranceAccount

    month = factory.SubFactory(MonthlyReport)
    name = factory.sequence(lambda n: 'Insurance {}'.format(n))
    type = random.choice([_[0] for _ in INSURANCE_TYPE])
    start_date = datetime.today()
    end_date = datetime.today() + timedelta(days=365)
    comments = 'Insurance comments'


class IncomeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Income

    month = factory.SubFactory(MonthlyReport)
    name = factory.sequence(lambda n: 'Income {}'.format(n))
    money = random.uniform(1, 1000)
    comments = 'Income comments'


class OutgoingFactory(factory.DjangoModelFactory):
    class Meta:
        model = Outgoing

    month = factory.SubFactory(MonthlyReport)
    name = factory.sequence(lambda n: 'Outgoing {}'.format(n))
    money = random.uniform(1, 1000)
    comments = 'Outgoing comments'
