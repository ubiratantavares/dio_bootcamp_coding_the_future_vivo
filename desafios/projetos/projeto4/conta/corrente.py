from projeto04.conta.conta import Conta

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