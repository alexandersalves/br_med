class ICurrencyDao:
    model = None

    def find_currency_id(self, abbreviation):
        '''
        Retorna o ID da instância de uma moeda
        Este método precisa criar o registro no banco caso ainda não exista
        '''


class IRateDao:
    model = None

    def add(self, item):
        '''
        Cria um novo registro
        '''
