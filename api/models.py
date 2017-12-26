from __future__ import unicode_literals

from django.db import models


class MonthReport(models.Model):
    date = models.DateField(blank=False, primary_key=True)
    total = models.IntegerField(default=0)
    income = models.IntegerField(default=0)
    outcome = models.IntegerField(default=0)


class Item(models.Model):
    month = models.ForeignKey(MonthReport, related_name='items')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    value = models.IntegerField()
    comment = models.TextField(blank=True)

    def __unicode__(self):
        return '{}, {}, {}'.format(self.name, self.type, self.value)


