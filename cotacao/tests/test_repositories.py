from unittest.mock import Mock

from django.test import TestCase

from cotacao.ports.dao import ICurrencyDao, IRateDao
from cotacao.repositories import CurrencyRepository


class CurrencyRepositoryTest(TestCase):

    def setUp(self):
        self.currency_id = 1
        self.data = {
            'date': '03-06-2022',
            'rates': {'BRL': 1.0},
        }

        currency_dao = Mock()
        currency_dao.return_value = Mock(spec=ICurrencyDao)
        currency_dao.return_value.find_currency_id.return_value \
            = self.currency_id
        rate_dao = Mock()
        rate_dao.return_value = Mock(spec=IRateDao)

        self.repository = CurrencyRepository(
            currency_dao,
            rate_dao,
        )

    def test_init(self):
        assert isinstance(
            self.repository.currency,
            ICurrencyDao,
        )
        assert isinstance(
            self.repository.rate,
            IRateDao,
        )

    def test_persist_rate(self):
        expected = {
            'date': '{}-{}-{}'.format(
                *self.data.get('date').split('-')[::-1],
            ),
            'amount': list(self.data.get('rates').values())[0],
            'currency_id': self.currency_id,
        }
        self.repository.persist_rate(self.data)
        self.repository.rate.add.assert_called_once_with(expected)

    def test_get_currency(self):
        currency_abbreviation = list(self.data.get('rates'))[0]
        self.repository._get_currency = Mock(
            side_effect=self.repository._get_currency,
        )
        self.repository.persist_rate(self.data)

        self.repository._get_currency.assert_called_once_with(
            currency_abbreviation,
        )
        self.repository.currency.find_currency_id.assert_called_once_with(
            currency_abbreviation,
        )
