
from modelos.heranca_multipla import Gato, Ornitorrinco
from modelos.heranca_simples import Caminhao, Carro, Motocicleta

def main():
    moto = Motocicleta("preta", "abc-1234", 2)
    carro = Carro("branco", "xde-0098", 4)
    caminhao = Caminhao("roxo", "gfd-8712", 8, True)
    print(moto)
    print(carro)
    print(caminhao)
    caminhao.exibe_carregado()
    gato = Gato(numero_patas=4, cor_pelo="preto")
    ornitorrinco = Ornitorrinco(cor_pelo="vermelho", cor_bico="laranja", numero_patas=2)
    print(gato)
    print(ornitorrinco)

if __name__ == "__main__":
    main()