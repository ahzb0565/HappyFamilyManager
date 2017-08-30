from __future__ import unicode_literals

from django.db import models
from .constants import *


class CashAndBackupAccount(models.Model):
    date = models.DateField(auto_created=True, auto_now_add=True)
    cash = models.FloatField(default=0)
    backup = models.FloatField(default=0)
    comments = models.TextField()


class InvestmentAccount(models.Model):
    date = models.DateField(auto_now_add=True)
    comments = models.TextField()


class InvestmentProduct(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, default=INVESTMENT_TYPE[0][0], choices=INVESTMENT_TYPE)
    capital = models.FloatField(default=0)
    current = models.FloatField(default=0)
    account = models.ForeignKey(InvestmentAccount)


class InsuranceAccount(models.Model):
    date = models.DateField(auto_now_add=True)
    comments = models.TextField()


class Insurance(models.Model):
    name = name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, default=INSURANCE_TYPE[0][0], choices=INSURANCE_TYPE)
    premium = models.FloatField(default=0)
    insured_amount = models.FloatField(default=0)
    total_input = models.FloatField(default=0)