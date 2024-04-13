class Animal:

    def __init__(self, numero_patas):
        self.__numero_patas = numero_patas

    @property
    def numero_patas(self):
        return self.__numero_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):

    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.__cor_pelo = cor_pelo

    @property
    def cor_pelo(self):
        return self.__cor_pelo
    
class Ave(Animal):

    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.__cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)


