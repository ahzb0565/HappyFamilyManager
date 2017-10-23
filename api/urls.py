from django.conf.urls import url
from .views import MonthlyReportView

urlpatterns = [
    url(r'^monthly_report/$', MonthlyReportView.as_view(), name='monthly-report'),
    url(r'^monthly_report/(?P<pk>\d+)/$', MonthlyReportView.as_view(), name='monthly-report-item'),
]