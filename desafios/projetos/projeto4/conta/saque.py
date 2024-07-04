from projeto04.conta.transacao import Transacao

class Saque(Transacao):
    
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        if conta.verificar_saque(self.valor):
            conta.historico.adicionar_transacao(self)