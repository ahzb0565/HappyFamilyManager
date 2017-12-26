import factory
from api.models import Item, MonthReport
from datetime import date, timedelta
import random


class MonthReportFactory(factory.DjangoModelFactory):
    class Meta:
        model = MonthReport
    date = date.today() - timedelta(days=random.randint(1, 100))
    total = 0
    income = 0
    outcome = 0


class ItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = Item

    month = factory.SubFactory(MonthReportFactory)

    name = factory.sequence(lambda n: 'item {}'.format(n))
    type = factory.sequence(lambda n: 'type {}'.format(n))
    comment = factory.sequence(lambda n: 'comments {}'.format(n))
    value = random.randint(1, 10000)
