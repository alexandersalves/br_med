from unittest.mock import Mock

from django.test import TestCase

from cotacao.ports.operator import IHttpOperator
from cotacao.ports.gateway import IRateGateway
from cotacao.use_cases import GetRateUseCase
from cotacao.repositories import CurrencyRepository


class GetRateUseCaseTest(TestCase):

    def setUp(self):
        operator = Mock()
        operator.return_value = Mock(spec=IHttpOperator)

        self.gateway = Mock()
        self.gateway.return_value = Mock(spec=IRateGateway)
        self.gateway.return_value.http = operator.return_value
        self.gateway.return_value.get_rate.return_value = {
            'date': '',
            'base': '',
            'rates': {},
        }

        self.use_case = GetRateUseCase(
            self.gateway,
            operator,
            Mock(),
            Mock(),
        )

        self.date = '03/06/2022'
        self.filters = {
            'currency_from': 'USD',
            'currency_to': 'BRL',
            'start_date': self.date,
            'end_date': self.date,
        }

    def test_init(self):
        assert isinstance(
            self.use_case.gateway,
            IRateGateway,
        )
        assert isinstance(
            self.use_case.gateway.http,
            IHttpOperator,
        )
        assert isinstance(
            self.use_case.repository,
            CurrencyRepository,
        )

    def test_execute(self):
        expected = [{
            'date': self.date.replace('/', '-'),
            'rates': {},
        }]

        response = self.use_case.execute(self.filters)
        assert response == expected

        reverse_date = '{}/{}/{}'.format(
            *self.date.split('/')[::-1]
        )
        self.use_case.gateway.get_rate.assert_called_once_with(
            reverse_date.replace('/', '-'),
            self.filters.get('currency_from'),
        )

    def test_get_dates(self):
        self.use_case._get_dates = Mock()
        self.use_case._get_dates.return_value = []

        self.use_case.execute(self.filters)
        self.use_case._get_dates.assert_called_once_with(
            **self.filters,
        )

    def test_persist(self):
        expected = {
            'date': self.date.replace('/', '-'),
            'rates': {},
        }
        self.use_case._persist_rate = Mock(
            side_effect=self.use_case._persist_rate,
        )
        self.use_case.repository.persist_rate = Mock()

        self.use_case.execute(self.filters)
        self.use_case._persist_rate.assert_called_once_with(expected)
        self.use_case.repository.persist_rate.assert_called_once_with(
            expected,
        )
