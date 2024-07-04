from operacao import Operacao
from local.estado import Estado
from local.municipio import Municipio
from local.bairro import Bairro
from local.endereco import Endereco

def executar_menu_principal(operacao):
    while True:
        opcao = operacao.apresentar_menu_principal()
        if opcao == 1:
            executar_menu_cliente(operacao)
        elif opcao == 2:
            executar_menu_conta(operacao)
        elif opcao == 3:
            break
        else:
            print("Operação inválida.")

def executar_menu_cliente(operacao):
    while True:
        opcao = operacao.apresentar_menu_cliente()
        if opcao == 1:
            print("Implementar Cadastrar")
        elif opcao == 2:
            print("Implementar Exibir")
        elif opcao == 3:
            print("Implementar Excluir")
        elif opcao == 4:
            print("Implementar Listar")
        elif opcao == 5:
            break
        else:
            print("Operação inválida.")

def executar_menu_conta(operacao):
    while True:
        opcao = operacao.apresentar_menu_conta()
        if opcao == 1:
            print("Implementar Cadastrar")
        elif opcao == 2:
            print("Implementar Depositar")
        elif opcao == 3:
            print("Implementar Sacar")
        elif opcao == 4:
            print("Implementar Extratificar")
        elif opcao == 5:
            print("Implementar Listar")
        elif opcao == 6:
            break
        else:
            print("Operação inválida.")


def main():
    #operacao = Operacao()
    #executar_menu_principal(operacao)
    estado = Estado("Rio de Janeiro", "RJ")
    municipio = Municipio("São Gonçalo", estado)
    bairro = Bairro("Arsenal", municipio)
    endereco = Endereco("Rua A", 220, "Casa 82", "24755-550", bairro)
    bairro.adicionar(endereco)
    municipio.adicionar(bairro)
    estado.adicionar(municipio)
    for endereco in bairro.enderecos:
        print(endereco)
    for bairro in municipio.bairros:
        print(bairro)
    for municipio in estado.municipios:
        print(municipio)


if __name__ == "__main__":
    main()
