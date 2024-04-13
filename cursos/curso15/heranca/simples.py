class Veiculo:

    def __init__(self, cor, placa, numero_rodas):
        self.__cor = cor
        self.__placa = placa
        self.__numero_rodas = numero_rodas

    @property
    def cor(self):
        return self.__cor
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def numero_rodas(self):
        return self.__numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.__carregado = carregado

    @property
    def carregado(self):
        return self.__carregado
    
    def exibe_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")

    