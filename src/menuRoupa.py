from cadastro import Cadastro
from cadastroRoupa import CadastroRoupa
from relatorio import Relatorio

class MenuRoupa():
    """ Modulo que contem a classe MenuRoupas """

    @staticmethod
    def menu_roupa(self, id_user):

        while (True):

            print("\n-----------------------------------------------\n")
            op = Cadastro.validarInteiro(self=Cadastro, mensagem="Digite a opcao desejada:\n\n1 - Cadastrar Roupa\n2 - Minhas roupas\n3 - Alterar Roupa\n4 - Excluir permanentemente\n5 - Sair\n")

            if (op == 1):
                print("\n-----------------------------------------------\n")
                CadastroRoupa().cadastrarRoupa(self=CadastroRoupa, id_user=id_user)

            elif (op == 2 or op == 3 or op == 4):

                print("\n-----------------------------------------------\n")
                Relatorio().roupasPorNome(self=Relatorio, id_user=id_user)

                if (op == 3):
                    CadastroRoupa().alterarRoupa(self=CadastroRoupa)

                elif (op == 4):
                    CadastroRoupa().removerRoupa(self=CadastroRoupa)

            elif (op == 5):
                exit()
            
            else:
                print("\nOpcao invalida!\n")
