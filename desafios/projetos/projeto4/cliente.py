
class Cliente:
    
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        self.__contas = []


    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self) -> str:
        return f"{self.nome}"

    