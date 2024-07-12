from operacao import Operacao
          
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
            print("Opção inválida.")            

def executar_menu_cliente(operacao):
    while True:
        opcao = operacao.apresentar_menu_cliente()
        if opcao == 1:
            operacao.cadastrar_cliente()
        elif opcao == 2:
            operacao.exibir_cliente()
        elif opcao == 3:
            operacao.excluir_cliente()
        elif opcao == 4:
            operacao.listar_clientes()
        elif opcao == 5:
            break
        else:
            print("Operação inválida.")

def executar_menu_conta(operacao):
    while True:
        opcao = operacao.apresentar_menu_conta()
        if opcao == 1:
            operacao.cadastrar_conta()
        elif opcao == 2:
            operacao.depositar_conta()
        elif opcao == 3:
            operacao.sacar_conta()
        elif opcao == 4:
            operacao.extratificar_conta()
        elif opcao == 5:
            operacao.listar_contas()
        elif opcao == 6:
            break
        else:
            print("Operação inválida.")

def main():
    operacao = Operacao()
    executar_menu_principal(operacao)

if __name__ == "__main__":
    main()
