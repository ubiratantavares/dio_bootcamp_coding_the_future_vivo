import datetime

class Historico:

    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionar_transacao(self, transacao):
        item = {"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now().strftime("%d/%m/%Y %H:%M:%s")}
        self.__transacoes.append(item)


