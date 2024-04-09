
class Estado:

    def __init__(self, nome, sigla):
        self.__nome = nome
        self.__sigla = sigla
        self.__municipios = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def municipios(self):
        return self.__municipios
    
    def adicionar(self, municipio):
        self.__municipios.append(municipio)

    def remover(self, municipio):
        self.__municipios.remove(municipio)
    
    def __str__(self):
        return f"{self.nome}"