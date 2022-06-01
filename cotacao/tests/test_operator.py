from unittest.mock import Mock

from django.test import TestCase

from cotacao.adapters.operator import RequestsHttpOperator


class RequestsHttpOperatorTest(TestCase):

    def setUp(self):
        self.operator = RequestsHttpOperator()

        self.mock_client = Mock()
        self.mocked_response = Mock()
        self.mocked_response.status_code = 200
        self.mocked_response.json.return_value = {}
        self.mock_client.get.return_value = self.mocked_response
        self.operator.client = self.mock_client

        self.options = {
            'url': 'http://test',
            'headers': {},
            'params': {},
            'payload': {},
        }

    def test_get(self):
        expected = {}
        assert self.operator.get(**self.options) == expected
        self.mock_client.get.assert_called_once_with(
            url=self.options['url'],
            headers=self.options['headers'],
            params=self.options['params'],
            json=self.options['payload'],
        )

    def test_get_not_200(self):
        expected_status_code = 400
        expected = 'Chamada inválida para {} ({})'.format(
            self.options.get('url'),
            expected_status_code,
        )
        self.mocked_response.status_code = expected_status_code
        self.assertRaisesMessage(
            Exception,
            expected,
            self.operator.get,
            **self.options,
        )
