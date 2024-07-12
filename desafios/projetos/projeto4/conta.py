from projeto4.conta.historico import Historico
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

class ContaCorrente(Conta):
    
    def __init__(self, numero, cliente, agencia, limite=500, limite_saques=3):
        super().__init__(numero, cliente, agencia)
        self.__limite = limite
        self.__limite_saques = limite_saques

    @property
    def limite(self):
        return self.__limite
    
    @property
    def limite_saques(self):
        return self.__limite_saques
    
    def verificar_saque(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        numero_saques > self.limite_saques
        if valor > self.limite or numero_saques > self.limite_saques:
            return False
        return True
    
    def __str__(self) -> str:
        return f"""Agência: {self.agencia}\nConta Corrente: {self.numero}\nCliente: {self.cliente.nome}"""