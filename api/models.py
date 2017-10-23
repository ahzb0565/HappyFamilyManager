from __future__ import unicode_literals

from django.db import models
from .constants import *


class MonthlyReport(models.Model):
    date = models.DateField(auto_now_add=True)
    comments = models.TextField()


class CashAndBackupAccount(models.Model):
    month = models.ForeignKey(MonthlyReport, related_name='cashes')
    name = models.CharField(max_length=50, blank=False)
    money = models.FloatField(default=0)
    comments = models.TextField()


class InvestmentAccount(models.Model):
    month = models.ForeignKey(MonthlyReport, related_name='investments')
    name = models.CharField(blank=False, max_length=50)
    money = models.FloatField(default=0)
    comments = models.TextField()


class InsuranceAccount(models.Model):
    month = models.ForeignKey(MonthlyReport, related_name='insurances')
    name = models.CharField(blank=False, max_length=50)
    type = models.CharField(max_length=10, default=INSURANCE_TYPE[0][0], choices=INSURANCE_TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.TextField()


class Income(models.Model):
    month = models.ForeignKey(MonthlyReport, related_name='incomes')
    name = models.CharField(blank=False, max_length=50)
    money = models.FloatField(default=0)
    comments = models.TextField()


class Outgoing(models.Model):
    month = models.ForeignKey(MonthlyReport, related_name='outgoings')
    name = models.CharField(blank=False, max_length=50)
    money = models.FloatField(default=0)
    comments = models.TextField()


