from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CurrentUser, AuthRoutes, FundViewSet


router = DefaultRouter()
router.register(r'funds', FundViewSet, base_name='fund')


urlpatterns = [
    path('currentUser/', CurrentUser.as_view()),
    path('auth_routes/', AuthRoutes.as_view()),
]

urlpatterns += router.urls
