from datetime import datetime

class Conta:

    def __init__(self, numero_agencia, saldo=0.):
        self.numero_agencia = numero_agencia
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def mostrar_saldo(self):
        return self.__saldo
    

class Foo:

    def __init__(self, x=None):
        self.__x = x

    @property
    def x(self):
        return self.__x or 0
    
    @x.setter
    def x(self, value):
        self.__x += value

    @x.deleter
    def x(self):
        self.__x = 0

class Pessoa:

    def __init__(self, nome, ano_nascimento):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ano_nascimento(self):
        return self.__ano_nascimento
    
    @property
    def idade(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento
    
    def __str__(self):
        return f"{self.nome} possui {self.idade} anos de idade."
    

        
    