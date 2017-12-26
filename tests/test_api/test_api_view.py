from django.test import TestCase
from django.urls.base import reverse
from tests.factories import ItemFactory, MonthReportFactory
from api.models import Item, MonthReport
from datetime import date


class ReportTestCase(TestCase):
    def test_create_report(self):
        response = self.client.get(reverse('api:create-report', kwargs={'day': date.today()}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MonthReport.objects.all().count(), 1)
        report = MonthReport.objects.first()
        self.assertEqual(report.date, date.today())
        self.assertEqual(report.total, 0)
        self.assertEqual(report.income, 0)
        self.assertEqual(report.outcome, 0)

    def test_delete_report(self):
        report = MonthReportFactory.create()
        response = self.client.get(reverse('api:delete-report', kwargs={'pk': report.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MonthReport.objects.all().count(), 0)

    def test_get_reports(self):
        report1 = MonthReportFactory.create()
        report2 = MonthReportFactory.create()
        response = self.client.get(reverse('api:get-reports'))
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(len(data), 2)
        self.assertEqual({i['date'] for i in data}, {report1.date.strftime('%Y-%m-%d'), report2.date.strftime('%Y-%m-%d')})

    def test_get_report(self):
        report = MonthReportFactory.create()
        response = self.client.get(reverse('api:get-report', kwargs={'pk': report.pk.strftime('%Y-%m-%d')}))
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['date'], report.date.strftime('%Y-%m-%d'))


class ItemTestCase(TestCase):

    def test_create_item_success(self):
        report = MonthReportFactory.create()
        data = {
            'month': report.pk,
            'name': 'item 1',
            'type': 'type 1',
            'value': 100,
            'comment': 'comments'
        }
        response = self.client.post(reverse('api:create-item'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.all().count(), 1)
        self.assertEqual(Item.objects.first().name, 'item 1')

    def test_delete_item_success(self):
        item = ItemFactory.create()
        response = self.client.get(reverse('api:delete-item', kwargs={'pk': item.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Item.objects.all().count(), 0)

    def test_get_item_success(self):
        item = ItemFactory.create()
        response = self.client.get(reverse('api:get-item', kwargs={'pk': item.id}))
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['id'], item.id)

    def test_get_items_success(self):
        item1 = ItemFactory.create()
        item2 = ItemFactory.create()
        response = self.client.get(reverse('api:get-items'))
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(len(data), 2)
        self.assertEqual({i['id'] for i in data}, {item1.id, item2.id})

