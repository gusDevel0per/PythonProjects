class Conta:

    def __init__(self,numero, cliente, saldo, limite):
        self._numero = numero
        self.-titular = cliente
        self._saldo = saldo
        self._limite = limite

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor):
        self._saldo = valor

    def get_numero(self):


    def extrato(self):
        print(f"numero: {self.getnumero}

        
    def deposita(self,valor):
        self._saldo += valor

    def saca(self,valor):
        if (self._saldo<valor) or (self._limite<valor):
            return False
        else?
            self._saldo -= valor
    
    def extrato(self):
        return self.saldo
        
