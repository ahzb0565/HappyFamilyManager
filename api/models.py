from __future__ import unicode_literals

from django.db import models
from .constants import *
from django.contrib.auth.models import User


class Deposit(models.Model):
    type = models.CharField(max_length=8, choices=CAPITAL_TYPE, default=CAPITAL_TYPE[0][0], blank=False)
    date = models.DateField(auto_now_add=True, auto_now=False)
    value = models.FloatField()
    author = models.ForeignKey(User)


class Insurance(models.Model):
    name = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=30)
    insurance_id = models.IntegerField()

    type = models.CharField(max_length=10, choices=INSURANCE_TYPE, default=INSURANCE_TYPE[0][0], blank=False)
    start_date = models.DateField(auto_now_add=True, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)

    premium = models.FloatField()
    ensured_amount = models.FloatField()

    bank_card = models.IntegerField()

    author = models.ForeignKey(User)
    status = models.CharField(max_length=12, choices=STATUS, default=STATUS[0][0], blank=False)


class InsuranceChangeLog(models.Model):
    belong_to = models.ForeignKey(Insurance, blank=False)
    payment = models.FloatField()
    date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=300)


class Fund(models.Model):
    name = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=30)
    fund_id = models.IntegerField()

    type = models.CharField(max_length=8, choices=FUNDS_TYPE, default=FUNDS_TYPE[0][0], blank=False)
    level = models.CharField(max_length=2, choices=LEVEL, default=LEVEL[0][0], blank=False)

    author = models.ForeignKey(User)


class FundChangeLog(models.Model):
    belong_to = models.ForeignKey(Fund, blank=False)
    principal = models.FloatField()
    current = models.FloatField()
    date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=300)


class Stock(models.Model):
    name = models.CharField(max_length=50, blank=False)
    stock_id = models.IntegerField()

    level = models.CharField(max_length=2, choices=LEVEL, default=LEVEL[0][0], blank=False)

    author = models.ForeignKey(User)


class StockChangeLog(models.Model):
    belong_to = models.ForeignKey(Stock, blank=False)
    principal = models.FloatField()
    current = models.FloatField()
    date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=300)


class Debt(models.Model):
    type = models.CharField(max_length=12, choices=DEBT_TYPE, default=DEBT_TYPE[0][0], blank=False)

    start_date = models.DateField(auto_now_add=True, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)
    status = models.CharField(max_length=12, choices=STATUS, default=STATUS[0][0], blank=False)

    author = models.ForeignKey(User)
    related = models.CharField(max_length=50)


class P2P(models.Model):
    name = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=30)

    level = models.CharField(max_length=1, choices=LEVEL, default=LEVEL[0][0], blank=False)

    author = models.ForeignKey(User)


class P2PChangeLog(models.Model):
    belong_to = models.ForeignKey(P2P, blank=False)
    principal = models.FloatField()
    current = models.FloatField()
    date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=300)