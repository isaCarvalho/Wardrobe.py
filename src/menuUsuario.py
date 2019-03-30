from cadastro import Cadastro
from cadastroUsuario import CadastroUsuario
from menuRoupa import MenuRoupa
from getpass import getpass
from relatorio import Relatorio

class MenuUsuario():
    """ Modulo que contem a classe MenuUsuario """

    def logar(self):
        """ Metodo que permite ao usuario fazer login """

        while (True):
            nome = Cadastro.validarString(self=Cadastro, mensagem="NOME DE USUARIO: ")
            senha =  getpass("SENHA: ")

            us = Cadastro.executarSelect(self=Cadastro, query="SELECT id_user FROM users WHERE nome = '{}' AND senha = '{}' AND ativo = 1".format(nome, senha))

            aux = [ tupla[0] for tupla in us ]

            if (aux != []):
                return aux[0]
            else:
                print("\n\n--------- Nome de usuario ou senha invalidos, ou o usuario foi desativado ---------\n\n")

    def menu_inicial(self):
        
        while (True):
            print("\n-----------------------------------------------\n")
            op = Cadastro.validarInteiro(self=Cadastro, mensagem="Digite a opcao desejada:\n\n1 - Entrar\n2 - Cadastrar\n3 - Sair\n")

            if (op == 1):
                return self.logar()

            elif (op == 2):
                CadastroUsuario().cadastrarUsuario(self=CadastroUsuario)
                print("\nUsuario cadastrado com sucesso!\n")
            
            elif (op == 3):
                exit()
            
            else:
                print("\nOpcao invalida!\n")

    def menu_principal(self):

        id_user = self.menu_inicial()

        if (id_user != 0):
            print("\nLogado com sucesso!\n")

            while (True):
                print("\n-----------------------------------------------\n")
                op = Cadastro().validarInteiro(mensagem="Digite a opcao desejada:\n\n1 - Meus dados\n2 - Alterar dados\n3 - Menu Roupas\n4 - Sair\n")
                
                if (op == 1):
                    Relatorio().imprimirPorId(self=Relatorio, id_user=id_user)

                elif (op == 2):
                    print("\n-----------------------------------------------\n")
                    CadastroUsuario().alterarUsuario(self=CadastroUsuario, id_usuario=id_user)
                    exit()

                elif (op == 3):
                    MenuRoupa().menu_roupa(self=MenuRoupa, id_user=id_user)

                elif (op == 4):
                    exit()

                else:
                    print("\nOpcao invalida!\n")
