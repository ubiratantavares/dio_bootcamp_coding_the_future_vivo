import textwrap

class Operacao:

    def __init__(self):
        pass

    def apresentar_menu_principal(self):
        menu = """\n================ MENU PRINCIPAL ================\n[1]\tCliente\n[2]\tConta Corrente\n[3]\tSair\n=> """
        return int(input(textwrap.dedent(menu)))

    def apresentar_menu_cliente(self):
        menu = """\n================ MENU CLIENTE ================\n[1]\tCadastrar\n[2]\tExibir\n[3]\tExcluir\n[4]\tListar\n[5]\tSair\n=> """
        return int(input(textwrap.dedent(menu)))
    
    def apresentar_menu_conta(self):
        menu = """\n================ MENU CONTA CORRENTE ================\n[1]\tCadastrar\n[2]\tDepositar\n[3]\tSacar\n[4]\tExtratificar\n[5]\tListar\n[6]\tSair\n=> """
        return int(input(textwrap.dedent(menu)))
           