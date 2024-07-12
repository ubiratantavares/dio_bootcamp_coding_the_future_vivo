import textwrap
from cliente import *
from endereco import *
class Operacao:

    def __init__(self):
        self.__clientes = []
        self.__contas = []
        self.__estado = Estado()
        self.__municipio = Municipio()
        self.__bairro = Bairro()
        self.__endereco = Endereco()

    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.__clientes.remove(cliente)

    def apresentar_menu_principal(self):
        opcoes = {1: "Cliente", 2: "Conta", 3: "Sair"}
        menu = "\n================ MENU PRINCIPAL ================\n"
        for chave, opcao in opcoes.items():
            menu += f"[{chave}]\t{opcao}\n"
        menu += "==> "
        return int(input(textwrap.dedent(menu)))

    def apresentar_menu_cliente(self):
        opcoes = {1: "Cadastrar", 2: "Exibir", 3: "Excluir", 4: "Listar", 5: "Sair"}
        menu = "\n================ MENU CLIENTE ================\n"
        for chave, opcao in opcoes.items():
            menu += f"[{chave}]\t{opcao}\n"
        menu += "==> "
        return int(input(textwrap.dedent(menu)))       

    def selecionar_cliente(self):
        opcoes = {1: "Física", 2: "Jurídica"}
        menu = "\n================ MENU PESSOA  ================\n"
        for chave, opcao in opcoes.items():
            menu += f"[{chave}]\t{opcao}\n"
        menu += "==> "
        return int(input(textwrap.dedent(menu)))
    

    def buscar_cpf(self, cpf):
        for cliente in self.__clientes:
            if isinstance(cliente, PessoaFisica):
                if cpf == cliente.get_cpf():
                    return cliente
        return None
    
    def cadastrar_cliente(self):
        opcao = self.selecionar_cliente()
        if opcao == 1:
            cliente = PessoaFisica()
            cliente.ler_cpf()
            cliente_buscado = self.buscar_cpf(cliente.get_cpf())
            if  cliente_buscado == None:                
                cliente.ler_nome()
                cliente.ler_data_nascimento()
                self.__endereco.ler_nome()
                self.__endereco.ler_numero()
                self.__endereco.ler_complemento()
                self.__endereco.ler_cep()
                self.__bairro.ler_nome()
                self.__municipio.ler_nome()
                self.__estado.ler_nome()
                self.__estado.ler_sigla()
                self.__municipio.set_estado(self.__estado)
                self.__bairro.set_municipio(self.__municipio)
                self.__endereco.set_bairro(self.__bairro)
                self.__estado.adicionar_municipio(self.__municipio)
                self.__municipio.adicionar_bairro(self.__bairro)
                self.__bairro.adicionar_endereco(self.__endereco)
                cliente.set_endereco(self.__endereco)
                self.adicionar_cliente(cliente)
                print("\nCliente cadastrado com sucesso.\n")
            else: 
                print(f"CPF {cliente.get_cpf()} já cadastrado.")
        elif opcao == 2:
            print("Implementar cadastro de pessoa jurídica")
        else:
            print("Opção inválida.")

    def exibir_cliente(self):
        if len(self.__clientes) != 0:
            opcao = self.selecionar_cliente()
            if opcao == 1:
                cliente = PessoaFisica()
                cliente.ler_cpf()
                cliente_buscado = self.buscar_cpf(cliente.get_cpf())
                if cliente_buscado != None:
                    print(cliente_buscado)
                else: 
                    print(f"CPF {cliente.get_cpf()} não encontrado")  
            elif opcao == 2:
                print("Implementar exibição de pessoa jurídica")
            else:
                print("Opção inválida.")
        else:
            print("Não há clientes cadastrados.")

    def excluir_cliente(self):
        if len(self.__clientes) != 0:
            opcao = self.selecionar_cliente()
            if opcao == 1:
                    cliente = PessoaFisica()
                    cliente.ler_cpf()
                    cliente_buscado = self.buscar_cpf(cliente.get_cpf())
                    if  cliente_buscado != None:
                        self.remover_cliente(cliente_buscado)
                    else: 
                        print(f"CPF {cliente.get_cpf()} não encontrado")  
            elif opcao == 2:
                print("Implementar exibição de pessoa jurídica")
            else:
                print("Opção inválida.")
        else:
            print("Não há clientes cadastrados")   

    def listar_clientes(self):
        if len(self.__clientes) != 0:
            opcao = self.selecionar_cliente()
            if opcao == 1:
                for cliente in self.__clientes:
                    if isinstance(cliente, PessoaFisica):
                        print(cliente)
            elif opcao == 2:
                for cliente in self.__clientes:
                    if isinstance(cliente, PessoaJuridica):
                        print(cliente)            
            else:
                print("Opção inválida.")
        else:
            print("Não há clientes cadastrados")   

    def apresentar_menu_conta(self):
        opcoes = {1: "Cadastrar", 2: "Depositar", 3: "Sacar", 4: "Extratificar", 5: "Listar", 6: "Sair"}
        menu = "\n================ MENU CONTA ================\n"
        for chave, opcao in opcoes.items():
            menu += f"[{chave}]\t{opcao}\n"
        menu += "==> "
        return int(input(textwrap.dedent(menu)))    

    def cadastrar_conta(self):
        pass

    def depositar_conta(self):
        pass

    def sacar_conta(self):
        pass

    def extratificar_conta(self):
        pass

    def listar_contas(self):
        pass