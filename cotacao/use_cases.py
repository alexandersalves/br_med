class GetRateUseCase:

    def __init__(self, gateway, operator):
        self.gateway = gateway(
            http=operator(),
        )

    def execute(self):
        return self.gateway.get_rate()
