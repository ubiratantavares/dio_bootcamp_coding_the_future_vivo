from abstrata import *

def mostrar(objetos):
    for objeto in objetos:
        print(objeto)

def main():
    e1 = Estudante("Guilherme", 1)
    e2 = Estudante("Giovanna", 2)
    estudantes = [e1, e2]
    mostrar(estudantes)
    Estudante.escola = "ALURA"
    e3 = Estudante("Chappie", 3)
    estudantes.append(e3)
    mostrar(estudantes)
    p = Pessoa.calcular_idade("Guilherme", 1973)
    print(p)
    print(Pessoa.e_maior_idade(p.idade))
    controle = ControleTV()
    controle.ligar()
    controle.desligar()
    print(controle.marca)
    controle = ControleArCondicionado()
    controle.ligar()
    controle.desligar()
    print(controle.marca)

    

if __name__ == "__main__":
    main()