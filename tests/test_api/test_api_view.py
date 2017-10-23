from django.test import TestCase
from django.urls.base import reverse
from tests.factories import MonthlyReportFactory, CashAndBackupAccountFactory, InsuranceAccountFactory, InvestmentAccountFactory,\
    IncomeFactory, OutgoingFactory
from api.models import MonthlyReport
from datetime import datetime, timedelta


class MonthlyReportTestCases(TestCase):
    def setUp(self):
        self.monthly_report = MonthlyReportFactory.create()
        CashAndBackupAccountFactory.create(month=self.monthly_report)
        InsuranceAccountFactory.create(month=self.monthly_report)
        InvestmentAccountFactory.create(month=self.monthly_report)
        IncomeFactory.create(month=self.monthly_report)
        OutgoingFactory.create(month=self.monthly_report)

    def test_cash_n_bk_view_get_list(self):
        response = self.client.get(reverse('api:monthly-report'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_cash_n_bk_view_get_item(self):
        response = self.client.get(reverse('api:monthly-report-item', kwargs={'pk': self.monthly_report.pk}))
        expected_result = {
            u"outgoings":[
                {
                    u"money":self.monthly_report.outgoings.first().money,
                    u"id":self.monthly_report.outgoings.first().id,
                    u"comments":u"Outgoing comments",
                    u"name":u"Outgoing 1"
                }
            ],
            u"insurances":[
                {
                    u"name":u"Insurance 1",
                    u"end_date":datetime.today() + timedelta(days=365),
                    u"comments":u"Insurance comments",
                    u"id":self.monthly_report.insurances.first().id,
                    u"type":u"accident",
                    u"start_date":datetime.today()
                }
            ],
            u"incomes":[
                {
                    u"money":self.monthly_report.incomes.first().money,
                    u"id":self.monthly_report.incomes.first().id,
                    u"comments":u"Income comments",
                    u"name":u"Income 1"
                }
            ],
            u"comments":u"comments 1",
            u"cashes":[
                {
                    u"money":self.monthly_report.cashes.first().money,
                    u"id":self.monthly_report.cashes.first().id,
                    u"comments":u"cash comments",
                    u"name":u"cash 1"
                }
            ],
            u"date":datetime.today(),
            u"investments":[
                {
                    u"money":self.monthly_report.investments.first().money,
                    u"id":self.monthly_report.investments.first().id,
                    u"comments":u"investment comments",
                    u"name":u"investment 1"
                }
            ],
            u"id":self.monthly_report.id
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], expected_result['id'])
        self.assertEqual(response.json()['outgoings'][0]['id'], expected_result['outgoings'][0]['id'])
        self.assertEqual(response.json()['insurances'][0]['id'], expected_result['insurances'][0]['id'])
        self.assertEqual(response.json()['cashes'][0]['id'], expected_result['cashes'][0]['id'])
        self.assertEqual(response.json()['investments'][0]['id'], expected_result['investments'][0]['id'])


    def test_cash_n_bk_view_get_item_404(self):
        id = self.monthly_report.pk
        MonthlyReport.objects.all().delete()
        response = self.client.get(reverse('api:monthly-report-item', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 404)

    def test_cash_n_bk_view_create(self):
        MonthlyReport.objects.all().delete()
        data = {
            'comments': 'comments'
        }
        response = self.client.post(reverse('api:monthly-report'), data=data)
        self.assertEqual(response.status_code, 201)
        result = MonthlyReport.objects.first()
        self.assertEqual(result.comments, 'comments')
