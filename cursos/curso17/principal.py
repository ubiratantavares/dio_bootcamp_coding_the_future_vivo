from poli import *

def plano_de_voo(objeto):
    objeto.voar()

def main():
    plano_de_voo(Pardal())
    plano_de_voo(Avestruz())

if __name__ == "__main__":
    main()

