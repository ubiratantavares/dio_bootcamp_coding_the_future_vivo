
class Municipio:

    def __init__(self, nome, estado):
        self.__nome = nome
        self.__estado = estado
        self.__bairros = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def bairros(self):
        return self.__bairros
    
    def adicionar(self, bairro):
        self.__bairros.append(bairro)

    def remover(self, bairro):
        self.__bairros.remove(bairro)
   
    def __str__(self) -> str:
        return f"{self.nome}"