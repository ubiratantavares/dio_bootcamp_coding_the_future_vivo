from abc import ABC, abstractmethod
import datetime
class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        pass

 
class Deposito(Transacao):
    
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor 
    
    def registrar(self, conta):
        if conta.verificar_valor(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        if conta.verificar_saque(self.valor):
            conta.historico.adicionar_transacao(self)

class Historico:

    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionar_transacao(self, transacao):
        item = {"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now().strftime("%d/%m/%Y %H:%M:%s")}
        self.__transacoes.append(item)