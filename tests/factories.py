import factory
from api.models import CashAndBackupAccount
from datetime import datetime
import random


class CashAndBackupAccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = CashAndBackupAccount
    cash = random.uniform(0, 101)
    backup = random.uniform(0, 101)
    comments = factory.sequence(lambda n: 'comments {}'.format(n))
    date = datetime.today()
