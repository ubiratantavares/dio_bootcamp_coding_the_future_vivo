from modelos.bicicleta import Bicicleta
from modelos.cachorro import Cachorro

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

def main():
    b1 = Bicicleta("vermelha", "caloi", 2022, 600)
    b1.buzinar()
    b1.correr()
    b1.parar()
    print(b1.cor, b1.modelo, b1.ano, b1.valor)

    b2 = Bicicleta("verde", "monark", 2000, 189)
    print(b2)
    b2.correr()

    c = Cachorro("Chappie", "amarelo")
    c.falar()

    print("Ola mundo")

    del c

    print("Ola mundo")
    print("Ola mundo")
    print("Ola mundo")

    criar_cachorro()

if __name__ == "__main__":
    main()