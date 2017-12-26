from django.conf.urls import url
from .views import ItemView, MonthReportView, account_types

urlpatterns = [
    url(r'^get_reports/$', MonthReportView.as_view({'get': 'list'}), name='get-reports'),
    url(r'^get_report/(?P<pk>[\d\-]+)/$', MonthReportView.as_view({'get': 'retrieve'}), name='get-report'),
    url(r'^create_report/(?P<day>[\d\-]+)/$', MonthReportView.as_view({'get': 'create'}), name='create-report'),
    url(r'^delete_report/(?P<pk>[\d\-]+)/$', MonthReportView.as_view({'get': 'delete'}), name='delete-report'),
    url(r'^get_acount_types/$', account_types, name='account-types'),

    url(r'^get_items/$', ItemView.as_view({'get': 'list'}), name='get-items'),
    url(r'^get_item/(?P<pk>\d+)/$', ItemView.as_view({'get': 'retrieve'}), name='get-item'),
    url(r'^create_item/$', ItemView.as_view({'post': 'create'}), name='create-item'),
    url(r'^delete_item/(?P<pk>\d+)/$', ItemView.as_view({'get': 'delete'}), name='delete-item'),
]