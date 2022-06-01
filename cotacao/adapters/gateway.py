from email import header
from cotacao.ports.gateway import IRateGateway


class VATcomplyRateGateway(IRateGateway):

    routes = {
        'base': 'https://api.vatcomply.com/rates',
    }

    @property
    def headers(self):
        return {}

    @property
    def params(self):
        return {
            'base': 'USD',
        }

    def get_rate(self):
        return self.http.get(
            url=self.routes.get('base'),
            headers=self.headers,
            params=self.params,
            payload={},
        )
