from datetime import datetime
from abc import ABC, abstractmethod
# variável de classe e variáveis de instância
class Estudante:

    escola = "DIO"

    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    def __str__(self):
        return f"{self.nome}, {self.matricula}, {self.escola}"
    
# métodos de classe e métodos estáticos
class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @classmethod
    def calcular_idade(cls, nome, ano_nascimento):
        return cls(nome, datetime.now().year - ano_nascimento)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

    def __str__(self):
        return f"{self.__nome}, {self.__idade}"
    

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass


class ControleTV(ControleRemoto):

    def ligar(self):
        print("Ligandp a TV...")
        print("TV ligada..")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada.")

    @property
    def marca(self):
        return "Philco"
    
class ControleArCondicionado(ControleRemoto):


    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ar Condicionado ligado..")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Ar Condicionado desligado.")

    @property
    def marca(self):
        return "LG"


