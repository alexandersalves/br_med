from datetime import datetime, timedelta


class GetRateUseCase:

    allowed_currencies = [
        'BRL',
        'USD',
        'EUR',
        'JPY',
    ]

    def __init__(self, gateway, operator):
        self.gateway = gateway(
            http=operator(),
        )

    def _get_dates(self, start_date, end_date, **kwargs):
        _min = datetime.strptime(start_date, '%d/%m/%Y')
        _max = datetime.strptime(end_date, '%d/%m/%Y')
        dates = []
        while _min <= _max:
            dates.append(_min.date())
            _min += timedelta(days=1)

        return dates

    def execute(self, filters):
        data = []
        for date in self._get_dates(**filters):
            response = self.gateway.get_rate(
                str(date),
                filters.get('currency_from'),
            )
            data.append({
                'date': date.strftime("%d-%m-%Y"),
                'rates': {
                    key: round(value, 2)
                    for key, value in response['rates'].items()
                    if all([
                        key in self.allowed_currencies,
                        key == filters.get('currency_from')
                        or key == filters.get('currency_to'),
                    ])
                },
            })
        return data
