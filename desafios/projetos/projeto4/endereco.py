class Estado:

    def __init__(self):
        self.__nome = ""
        self.__sigla = ""
        self.__municipios = []

   
    def ler_nome(self):
        self.__nome = input("Digite o estado: ")
    
    def ler_sigla(self):
        self.__sigla = input("Digite a sigla do estado: ")
   
    def adicionar_municipio(self, municipio):
        self.__municipios.append(municipio)

    def remover_municipio(self, municipio):
        self.__municipios.remove(municipio)

    def listar_municipios(self):
        for municipio in self.municipios:
            print(municipio)
    
    def __str__(self):
        return f"{self.__nome}/{self.__sigla}"
    
class Municipio:

    def __init__(self):
        self.__nome = ""
        self.__estado = None
        self.__bairros = []    

    def ler_nome(self):
        self.__nome = input("Digite o município: ")

    def set_estado(self, estado):
        self.__estado = estado
    
    def adicionar_bairro(self, bairro):
        self.__bairros.append(bairro)

    def remover_bairro(self, bairro):
        self.__bairros.remove(bairro)

    def listar_bairros(self):
        for bairro in self.bairros:
            print(bairro)
   
    def __str__(self):
        return f"{self.__nome}, {self.__estado}"

class Bairro:

    def __init__(self):
        self.__nome = ""
        self.__municipio = None
        self.__enderecos = []
   
    def ler_nome(self):
        self.__nome = input("Digite o bairro: ")

    def set_municipio(self, municipio):
        self.__municipio = municipio

    def adicionar_endereco(self, endereco):
        self.__enderecos.append(endereco)

    def remover_endereco(self, endereco):
        self.__enderecos.remove(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)
    
    def __str__(self):
        return f"{self.__nome}, {self.__municipio}"

class Endereco:
    
    def __init__(self):
        self.__nome = ""
        self.__numero = "" 
        self.__complemento = ""
        self.__cep = ""
        self.__bairro = None
    
    def ler_nome(self):
        self.__nome = input("Digite o logradouro: ")
        
    def ler_numero(self):
        self.__numero = input("Digite o numero: ")

    def ler_complemento(self):
        self.__complemento = input("Digite o complemento: ")

    def ler_cep(self):
        self.__cep = input("Digite o CEP: ")

    def set_bairro(self, bairro):
        self.__bairo = bairro

    def __str__(self):
        return f"{self.__nome}, {self.__numero}, {self.__complemento}, {self.__bairro} - CEP: {self.__cep}"