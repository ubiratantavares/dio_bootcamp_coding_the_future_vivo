
class Endereco:
    
    def __init__(self, logradouro, numero, complemento, cep, bairro):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento
        self.__cep = cep
        self.__bairro = bairro

    @property
    def logradouro(self):
        return self.__logradouro
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def complemento(self):
        return self.__complemento
    
    @property
    def cep(self):
        return self.__cep
    
    @property
    def bairro(self):
        return self.__bairro    

    def __str__(self):
        return f"""{self.logradouro}, {self.numero}, {self.complemento}, {self.bairro}, {self.bairro.municipio}/{self.bairro.municipio.estado.sigla} - CEP: {self.cep}"""