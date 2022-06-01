from rest_framework.response import Response
from rest_framework.views import APIView

from cotacao.use_cases import GetRateUseCase
from cotacao.adapters.gateway import VATcomplyRateGateway
from cotacao.adapters.operator import RequestsHttpOperator


class GetRateView(APIView):
    def get(self, request):
        try:
            use_case = GetRateUseCase(
                gateway=VATcomplyRateGateway,
                operator=RequestsHttpOperator,
            )
            response = use_case.execute()
        except Exception as error:
            raise Response(error, 400)
        return Response(response)
