from modelos.encapsulamento import *

def main():
    
    conta = Conta("0001", 100)
    conta.depositar(100)
    print(conta.numero_agencia)
    print(conta.mostrar_saldo())

    foo = Foo(10)
    print(foo.x)
    del foo.x
    print(foo.x)
    foo.x = 10
    print(foo.x)

    pessoa = Pessoa("Guilherme", 1994)
    print(pessoa)

if __name__ == "__main__":
    main()

