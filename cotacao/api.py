from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from cotacao.use_cases import GetRateUseCase
from cotacao.adapters.dao import RateDao, CurrencyDao
from cotacao.adapters.gateway import VATcomplyRateGateway
from cotacao.adapters.operator import RequestsHttpOperator
from cotacao.serializers import (
    GetRateSerializer,
    CurrencySerializer,
    RateSerializer,
)
from cotacao.models import Currency, Rate
from cotacao.filters import CurrencyFilter, RateFilter


class GetRateView(APIView):
    def get(self, request):
        serializer = GetRateSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        try:
            use_case = GetRateUseCase(
                gateway=VATcomplyRateGateway,
                operator=RequestsHttpOperator,
                currency_dao=CurrencyDao,
                rate_dao=RateDao,
            )
            response = use_case.execute(serializer.data)
        except Exception as error:
            return Response(str(error), 400)
        return Response(response)


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.AllowAny]
    filter_class = CurrencyFilter


class RateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [permissions.AllowAny]
    filter_class = RateFilter
