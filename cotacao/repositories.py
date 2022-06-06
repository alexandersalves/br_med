from datetime import datetime


class CurrencyRepository:

    def __init__(self, currency_dao, rate_dao):
        self.currency = currency_dao()
        self.rate = rate_dao()

    def _get_currency(self, abbreviation):
        try:
            return self.currency.find_currency_id(abbreviation)
        except Exception as e:
            raise Exception(f'ID da moeda {abbreviation} indisponível.')

    def persist_rate(self, data):
        for abbreviation, amount in data.get('rates').items():
            date = datetime.strptime(
                data.get('date'), '%d-%m-%Y',
            ).strftime('%Y-%m-%d')
            item = {
                'date': date,
                'amount': amount,
                'currency_id': self._get_currency(abbreviation),
                'base_id': self._get_currency(data.get('base')),
            }

            if data.get('base') == abbreviation:
                continue

            try:
                self.rate.add(item)
            except Exception as e:
                raise Exception('Não foi possível persistir os dados.')
