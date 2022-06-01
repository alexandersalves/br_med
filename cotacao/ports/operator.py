class IHttpOperator:

    client = None

    def get(self, url, headers, params, payload):
        '''
        Resultado de requisição HTTP com método GET
        '''
