from email import header
from cotacao.ports.gateway import IRateGateway


class VATcomplyRateGateway(IRateGateway):

    _routes = {
        'base': 'https://api.vatcomply.com/rates',
    }

    @property
    def _headers(self):
        return {}

    def get_rate(self, date, currency='USD'):
        params = {
            'base': currency,
            'date': date,
        }
        return self.http.get(
            url=self._routes.get('base'),
            headers=self._headers,
            params=params,
            payload={},
        )
