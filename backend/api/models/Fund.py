from django.db import models


# Financing
class Fund(models.Model):
    company = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=20, blank=False)
    fund_id = models.IntegerField(blank=True)
    type = models.CharField(max_length=10, blank=False)
