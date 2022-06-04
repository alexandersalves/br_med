from unittest.mock import Mock

from django.test import TestCase

from cotacao.adapters.dao import CurrencyDao, RateDao
from cotacao.models import Currency, Rate


class CurrencyDaoTest(TestCase):

    def setUp(self):
        self.abbreviation = 'BRL'
        self.currency_id = 1
        self.currency_dao = CurrencyDao()

    def test_init(self):
        assert isinstance(
            self.currency_dao.model(),
            Currency,
        )

    def test_find_currency_id_only_creating(self):
        assert Currency.objects.count() == 0
        currency_id = self.currency_dao.find_currency_id(self.abbreviation)
        assert Currency.objects.count() == 1
        assert Currency.objects.first().id == currency_id

    def test_find_currency_id_only_finding(self):
        Currency.objects.create(
            id=self.currency_id,
            abbreviation=self.abbreviation,
        )
        assert self.currency_dao.find_currency_id(self.abbreviation) \
            == self.currency_id


class RateDaoTest(TestCase):

    def setUp(self):
        self.currency = Currency.objects.create(
            id=1,
            abbreviation='BRL',
        )

        self.item = {
            'date': '2022-06-03',
            'amount': 1.0,
            'currency_id': self.currency.id,
        }

        self.rate_dao = RateDao()

    def test_init(self):
        assert isinstance(
            self.rate_dao.model(),
            Rate,
        )

    def test_add(self):
        assert Rate.objects.count() == 0
        rate = self.rate_dao.add(self.item)
        assert Rate.objects.count() == 1
        assert Rate.objects.first() == rate
