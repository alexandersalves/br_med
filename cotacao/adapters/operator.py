import requests

from cotacao.ports.operator import IHttpOperator


class RequestsHttpOperator(IHttpOperator):

    client = requests

    def get(self, url, headers, params, payload):
        response = self.client.get(
            url=url,
            headers=headers,
            params=params,
            json=payload,
        )

        if response.status_code == 200:
            return response.json()

        raise Exception(
            f'Chamada inválida para {url} ({response.status_code}).'
        )
