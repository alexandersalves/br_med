class IRateGateway:

    def __init__(self, http):
        self.http = http
        '''
        Requer um operador de requisições HTTP
        '''

    def get_rate(self, date, currency):
        '''
        Busca cotações em uma API
        '''
