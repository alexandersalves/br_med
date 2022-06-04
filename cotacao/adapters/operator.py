import requests

from cotacao.ports.operator import IHttpOperator


class RequestsHttpOperator(IHttpOperator):

    _client = requests

    def get(self, url, headers, params, payload):
        response = self._client.get(
            url=url,
            headers=headers,
            params=params,
            json=payload,
        )

        if response.status_code == 200:
            return response.json()

        # Retornar a url é uma falha de segurança,
        # mantida para fins informativos.
        raise Exception(
            f'Chamada inválida para {url} ({response.status_code}).'
        )
