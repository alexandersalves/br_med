from datetime import datetime, timedelta

from cotacao.repositories import CurrencyRepository


class GetRateUseCase:

    _allowed_currencies = [
        'BRL',
        'USD',
        'EUR',
        'JPY',
    ]

    def __init__(self, gateway, operator, currency_dao, rate_dao):
        self.gateway = gateway(
            http=operator(),
        )
        self.repository = CurrencyRepository(
            currency_dao=currency_dao,
            rate_dao=rate_dao,
        )

    def _persist_rate(self, data):
        self.repository.persist_rate(data)

    def _get_dates(self, start_date, end_date, **kwargs):
        _min = datetime.strptime(start_date, '%d/%m/%Y')
        _max = datetime.strptime(end_date, '%d/%m/%Y')
        dates = []
        while _min <= _max:
            dates.append(_min.date())
            _min += timedelta(days=1)

        return dates

    def execute(self, filters):
        currency_from = filters.get('currency_from')
        currency_to = filters.get('currency_to')
        if any([
            currency_from not in self._allowed_currencies,
            currency_to not in self._allowed_currencies,
        ]):
            raise Exception('Moeda inválida.')

        result = []
        for date in self._get_dates(**filters):
            response = self.gateway.get_rate(
                str(date),
                filters.get('currency_from'),
            )
            item = {
                'date': date.strftime("%d-%m-%Y"),
                'rates': {
                    key: round(value, 2)
                    for key, value in response['rates'].items()
                    if any([
                        key == currency_from,
                        key == currency_to,
                    ])
                },
            }
            result.append(item)
            # TODO: Deveria ser persistido com delay
            self._persist_rate(item)
        return result
