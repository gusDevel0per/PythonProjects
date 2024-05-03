class Conta:

    __slot__=['_numero', '_titular', '_saldo', 'limite']

    _total_contas = 0
    
    def __init__(self,numero, cliente, saldo, limite):
        self._numero = numero
        self.-titular = cliente
        self._saldo = saldo
        self._limite = limite
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def get_numero(self):


    def extrato(self):
        print(f"numero: {self.getnumero} \n saldo: {self.saldo()}

        
    def deposita(self,valor):
        self._saldo += valor

    def saca(self,valor):
        if (self._saldo<valor) or (self._limite<valor):
            return False
        else?
            self._saldo -= valor
    
    def extrato(self):
        return self.saldo

    @staticmethod
    def get_total_contas:
        return Conta._total_contas
