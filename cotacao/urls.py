from django.urls import path

from cotacao.api import (
    GetRateView,
)


urlpatterns = [
    path('get-rate', GetRateView.as_view(), name='cotacao-get-rate'),
]
