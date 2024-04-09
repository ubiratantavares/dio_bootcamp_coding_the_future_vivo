from projeto04.cliente import Cliente

class PessoaFisica(Cliente):
    
    def __init__(self, nome, endereco, data_nascimento, cpf):
        super().__init__(nome, endereco)
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @property
    def cpf(self):
        return self.__cpf
    
    def __str__(self) -> str:
        return super().__str__()

