class Cliente:
    
    def __init__(self):
        self.__nome = ""
        self.__endereco = None
        self.__contas = []

    def ler_nome(self):
        self.__nome = input("Digite o nome do cliente: ")

    def get_nome(self):
        return self.__nome
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def remover_conta(self, conta):
        self.__contas.remove(conta)

    def listar_contas(self):
        for conta in self.__contas:
            print(conta)

    def __str__(self) -> str:
        return f"Nome: {self.__nome}\nEndereco: {self.__endereco}"
    
class PessoaFisica(Cliente):
    
    def __init__(self):
        super().__init__()
        self.__data_nascimento = ""
        self.__cpf = ""

    def get_cpf(self):
        return self.__cpf

    def ler_data_nascimento(self):
        self.__data_nascimento = input("Digite a data de nascimento: ")

    def ler_cpf(self):
        self.__cpf = input("Digite o CPF: ")
    
    def __str__(self) -> str:
        return super().__str__() + f"\nData de nascimento: {self.__data_nascimento}\nCPF: {self.__cpf}"
    

class PessoaJuridica(Cliente):
    
    def __init__(self):
        super().__init__()
        self.__cnpj = ""

    def get_cnpj(self):
        return self.__cnpj

    def ler_cnpj(self):
        self.__cnpj = input("Digite o CNPJ: ")
    
    def __str__(self) -> str:
        return super().__str__() + f"\nCNPJ: {self.__cnpj}"
