from django.test import TestCase
from django.urls.base import reverse
from tests.factories import CashAndBackupAccountFactory
from api.models import CashAndBackupAccount


class CashAndBackupAccountViewTestCase(TestCase):
    def setUp(self):
        self.cash_n_bk_a = CashAndBackupAccountFactory.create()

    def test_cash_n_bk_view_get_list(self):
        response = self.client.get(reverse('api:cash-and-backup'))
        expected_result = {
            u'date': unicode(self.cash_n_bk_a.date),
            u'cash': self.cash_n_bk_a.cash,
            u'id': self.cash_n_bk_a.id,
            u'backup': self.cash_n_bk_a.backup,
            u'comments': unicode(self.cash_n_bk_a.comments),
        }
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json()[0], expected_result)

    def test_cash_n_bk_view_get_item(self):
        response = self.client.get(reverse('api:cash-and-backup-item', kwargs={'pk': self.cash_n_bk_a.pk}))
        expected_result = {
            u'date': unicode(self.cash_n_bk_a.date),
            u'cash': self.cash_n_bk_a.cash,
            u'id': self.cash_n_bk_a.id,
            u'backup': self.cash_n_bk_a.backup,
            u'comments': unicode(self.cash_n_bk_a.comments),
        }
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), expected_result)

    def test_cash_n_bk_view_get_item_404(self):
        id = self.cash_n_bk_a.pk
        CashAndBackupAccount.objects.all().delete()
        response = self.client.get(reverse('api:cash-and-backup-item', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 404)

    def test_cash_n_bk_view_create(self):
        CashAndBackupAccount.objects.all().delete()
        data = {
            'cash': 120,
            'backup': 110,
            'comments': 'comments'
        }
        response = self.client.post(reverse('api:cash-and-backup'), data=data)
        self.assertEqual(response.status_code, 201)
        result = CashAndBackupAccount.objects.first()
        self.assertEqual(result.cash, 120.0)
        self.assertEqual(result.backup, 110.0)
        self.assertEqual(result.comments, 'comments')
