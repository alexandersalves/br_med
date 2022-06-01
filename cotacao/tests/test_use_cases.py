from unittest.mock import Mock

from django.test import TestCase

from cotacao.ports.operator import IHttpOperator
from cotacao.ports.gateway import IRateGateway
from cotacao.use_cases import GetRateUseCase


class GetRateUseCaseTest(TestCase):

    def setUp(self):
        operator = Mock()
        operator.return_value = Mock(spec=IHttpOperator)

        self.gateway = Mock()
        self.gateway.return_value = Mock(spec=IRateGateway)
        self.gateway.return_value.http = operator.return_value

        self.use_case = GetRateUseCase(
            self.gateway,
            operator,
        )

    def test_init(self):
        assert isinstance(
            self.use_case.gateway,
            IRateGateway,
        )
        assert isinstance(
            self.use_case.gateway.http,
            IHttpOperator,
        )

    def test_execute(self):
        expected = {
            'date': '',
            'base': '',
            'rates': {},
        }
        self.gateway.return_value.get_rate.return_value = expected
        response = self.use_case.execute()
        assert response == expected
        self.use_case.gateway.get_rate.assert_called_once_with()
