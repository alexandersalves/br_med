from unittest import expectedFailure
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
        assert self.gateway.headers == expected

    def test_params(self):
        expected = {
            'base': 'USD',
        }
        assert self.gateway.params == expected

    def test_get_rate(self):
        expected = {
            'date': '',
            'base': '',
            'rates': {},
        }
        self.http.get.return_value = expected
        assert self.gateway.get_rate() == expected
