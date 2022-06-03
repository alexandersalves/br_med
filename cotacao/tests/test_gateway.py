from email import header
from unittest.mock import Mock

from django.test import TestCase

from cotacao.adapters.gateway import VATcomplyRateGateway


class VATcomplyRateGatewayTest(TestCase):

    def setUp(self):
        self.http = Mock()
        self.gateway = VATcomplyRateGateway(http=self.http)

    def test_init(self):
        assert self.gateway.http == self.http

    def test_headers(self):
        expected = {}
        assert self.gateway._headers == expected

    def test_http_call(self):
        expected_url = self.gateway._routes.get('base')
        expected_params = {
            'base': 'USD',
            'date': 'dumb-date-test',
        }
        self.gateway.get_rate(expected_params.get('date'))
        self.gateway.http.get.assert_called_once_with(
            url=expected_url,
            params=expected_params,
            headers={},
            payload={},
        )

    def test_get_rate(self):
        expected = {
            'date': '',
            'base': '',
            'rates': {},
        }
        self.http.get.return_value = expected
        assert self.gateway.get_rate('dumb-date-test') == expected
