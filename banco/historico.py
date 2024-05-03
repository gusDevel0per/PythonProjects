import datetime

class Historico:

    def __init__(self, transacoes):
        self.data_da_abertura = datetime.datetime.now()

    def imprime(self):
        
