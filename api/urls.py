from django.conf.urls import url
from .views import CashAndBackupAccountView

urlpatterns = [
    url(r'^cash_and_backup/$', CashAndBackupAccountView.as_view(), name='cash-and-backup'),
    url(r'^cash_and_backup/(?P<pk>\d+)/$', CashAndBackupAccountView.as_view(), name='cash-and-backup-item'),
]