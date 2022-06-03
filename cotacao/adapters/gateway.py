from email import header
from cotacao.ports.gateway import IRateGateway


class VATcomplyRateGateway(IRateGateway):

    routes = {
        'base': 'https://api.vatcomply.com/rates',
    }

    @property
    def headers(self):
        return {}

    def get_rate(self, date, currency='USD'):
        params = {
            'base': currency,
            'date': date,
        }
        return self.http.get(
            url=self.routes.get('base'),
            headers=self.headers,
            params=params,
            payload={},
        )
