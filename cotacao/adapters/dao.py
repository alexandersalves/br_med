from cotacao.models import Currency, Rate

from cotacao.ports.dao import ICurrencyDao, IRateDao


class CurrencyDao(ICurrencyDao):
    model = Currency

    def find_currency_id(self, abbreviation):
        currency, _ = self.model.objects.get_or_create(
            abbreviation=abbreviation.upper(),
        )
        return currency.id


class RateDao(IRateDao):
    model = Rate

    def add(self, item):
        rate, _ = self.model.objects.get_or_create(
            date=item.get('date'),
            currency_id=item.get('currency_id'),
            defaults=item,
        )
        return rate
