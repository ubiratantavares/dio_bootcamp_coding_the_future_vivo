
class Bairro:

    def __init__(self, nome, municipio):
        self.__nome = nome
        self.__municipio = municipio
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def municipio(self):
        return self.__municipio
    
    @property
    def enderecos(self):
        return self.__enderecos

    def adicionar(self, endereco):
        self.__enderecos.append(endereco)

    def remover(self, endereco):
        self.__enderecos.remove(endereco)

    
    def __str__(self):
        return f"{self.nome}"

