from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cotacao.api import (
    GetRateView,
    CurrencyViewSet,
    RateViewSet,
)


router = DefaultRouter()
router.register('currencies', CurrencyViewSet, basename='cotacao-currency')
router.register('rates', RateViewSet, basename='cotacao-rate')

urlpatterns = [
    path('get-rate/', GetRateView.as_view(), name='cotacao-get-rate'),
    path('', include(router.urls)),
]
