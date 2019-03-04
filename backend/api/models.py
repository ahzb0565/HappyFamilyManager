from django.db import models


# Income
class Income(models.Model):
    date = models.DateField(auto_now_add=True)
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    comments = models.TextField()


# Cash
class Cash(models.Model):
    date = models.DateField(auto_now_add=True)
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    name = models.CharField(max_length=20, blank=False)


# Backup
class Backup(models.Model):
    name = models.CharField(max_length=20, blank=False)
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    comments = models.TextField()


# Insurance
class Insurance(models.Model):
    number = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=20, blank=False)
    coverage = models.IntegerField(blank=False)
    premium = models.IntegerField(blank=False)
    type = models.CharField(max_length=30, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()


# borrow and lend
class Borrow(models.Model):
    object = models.CharField(max_length=20)
    type = models.CharField()
    number = models.CharField(max_length=50, blank=False)
    borrow_date = models.DateField(auto_now_add=True)
    pay_back_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)


class Lend(models.Model):
    object = models.CharField(max_length=20)
    type = models.CharField()
    number = models.CharField(max_length=50, blank=False)
    lent_date = models.DateField(auto_now_add=True)
    get_back_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)


# Debt
class Debt(models.Model):
    type = models.CharField()
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    total_number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    bank = models.CharField(max_length=30)
    status = models.CharField()


# Spend
class SpendMoney(models.Model):
    date = models.DateField(auto_now_add=True)
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    comments = models.TextField()


class SpendInsurance(models.Model):
    date = models.DateField(auto_now_add=True)
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    insurance = models.ForeignKey(to=Insurance, blank=False)
    comments = models.TextField()


class SpendPayBack(models.Model):
    date = models.DateField(auto_now_add=True)
    number = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    debt = models.ForeignKey(to=Borrow, blank=False)
    comments = models.TextField()


# Financing
class Fund(models.Model):
    company = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=20, blank=False)
    type = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    capital = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    value = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    status = models.CharField(max_length=20)


class P2P(models.Model):
    company = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=20, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    capital = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    interest = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    status = models.CharField(max_length=20)