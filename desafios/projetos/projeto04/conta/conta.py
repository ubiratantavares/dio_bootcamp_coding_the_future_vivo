from projeto04.conta.historico import Historico
class Conta:
    
    def __init__(self, numero, cliente, agencia):
        self.__numero = numero
        self.__cliente = cliente
        self.__agencia = agencia
        self.__historico = Historico()
        self.__saldo = 0

    @property
    def numero(self):
        return self.__numero
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def historico(self):
        return self.__historico
        
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    def verificar_valor(self, valor):
        if valor > 0:
            return True
        return False
    
    def verificar_saque(self, valor):
        if self.saldo >= valor:
            return True
        return False
    
    def sacar(self, valor):
        self.saldo -= valor
        
    def depositar(self, valor):
        self.saldo += valor

