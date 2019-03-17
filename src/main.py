""" Modulo principal do programa """

from menuUsuario import MenuUsuario
from relatorio import Relatorio
from cadastro import Cadastro

def main():

    while (True):
        print("\n-----------------------------------------------\n")
        op = Cadastro.validarInteiro(self=Cadastro, mensagem="Digite a opcao desejada:\n\n1 - Menu de usuario\n2 - Relatorios\n3 - Sair\n")

        if (op == 1):
            MenuUsuario().menu_principal()

        elif (op == 2):
            
            print("\n-----------------------------------------------\n")
            op1 = Cadastro.validarInteiro(self=Cadastro, mensagem="Digite a opcao desejada:\n\n1 - Visualizar\n2 - Estatisticas\n")
            
            if (op1 == 1):
                Relatorio().imprimirUsuarios(self=Relatorio)
                Relatorio().imprimirRoupas(self=Relatorio)

            elif (op1 == 2):
                print("\n-----------------------------------------------\n")
                op2 = Cadastro.validarInteiro(self=Cadastro, mensagem="Digite a opcao desejada:\n\n1 - Grafico de roupas por usuarios\n2 - Porcentagens\n")                
                
                if (op2 == 1):
                    Relatorio().g_roupasPorUsuario(self=Relatorio)

                elif (op2 == 2):
                    Relatorio().porcentagens(self=Relatorio)
                else:
                    print("\nOpcao invalida!\n")

        elif (op == 3):
            exit()

        else:
            print("\nOpcao invalida!\n")
            

main()