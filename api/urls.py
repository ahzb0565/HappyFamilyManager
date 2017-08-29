from django.conf.urls import url
from .views import API1

urlpatterns = [
    url(r'^api1/$', API1.as_view(), name='api1'),
]