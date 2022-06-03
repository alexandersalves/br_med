from rest_framework.response import Response
from rest_framework.views import APIView

from cotacao.use_cases import GetRateUseCase
from cotacao.adapters.gateway import VATcomplyRateGateway
from cotacao.adapters.operator import RequestsHttpOperator
from cotacao.serializers import GetRateSerializer


class GetRateView(APIView):
    def get(self, request):
        serializer = GetRateSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        try:
            use_case = GetRateUseCase(
                gateway=VATcomplyRateGateway,
                operator=RequestsHttpOperator,
            )
            response = use_case.execute(serializer.data)
        except Exception as error:
            return Response(str(error), 400)
        return Response(response)
