"""
Modulo que contem a classe Relatorio.

Esta classe contera as seguintes funcionalidades:

1 - Imprimir os usuarios em ordem alfabetica
2 - Impirmir a tabela com todas as roupas
2.1 - Imprimir as roupas por categoria
2.2 - Imprimir as roupas por tamanho
2.3 - Imprimir as roupas de um determinado usuario por id
3 - Gerar gráfico e imprimir a quantidade de roupas por usuario
4 - Gerar porcentagem de roupas por categorias
5 - Gerar porcentagem de roupas por tamanho
6 - Gerar relacao de roupas desativadas
7 - Gerar relacao de usuarios desativados
"""

from cadastro import Cadastro
from usuario import Usuario

import pandas as pd
import matplotlib.pyplot as plt

class Relatorio():

    """ Classe Relatorio """

    """ Usuarios """

    def listaSelect(query):
        return [ tupla[0] for tupla in Cadastro.executarSelect(self=Cadastro, query=query) ]

    @staticmethod
    def usuarios(self):
        """ Metodo que constroi o DataFrame com todos os campos do usuario """

        dic = {
            "ID_USER": self.listaSelect(query="SELECT id_user FROM users"), 
            "NOME": self.listaSelect(query="SELECT nome FROM users"),
            "EMAIL": self.listaSelect(query="SELECT email FROM users"),
            "SENHA": self.listaSelect(query="SELECT senha FROM users"),
            "ATIVO": self.listaSelect(query="SELECT ativo FROM users")
        }

        return pd.DataFrame(dic)

    @staticmethod
    def imprimirPorId(self, id_user):
        """ Metodo que imprime todos os campos de um usuario por id """
        # Trocar para pesquisar no dataframe depois
        print(Cadastro().executarSelect(query="SELECT * FROM users WHERE id_user = {:d}".format(id_user)))
    
    @staticmethod
    def imprimirUsuarios(self):
        """ Metodo que imprime todos os usuarios ordenados por nome """

        t_user = self.usuarios(self=Relatorio)
        
        user = t_user.loc[:, ["ID_USER", "NOME", "EMAIL"]]

        print("\n-----------------------------------------------\n")
        print(user.sort_values(by="NOME"))
        print("\n-----------------------------------------------\n")
   
    """ Roupas """

    @staticmethod
    def roupas(self):
        """ Metodo que constroi o DataFrame das roupas """

        dic = {
            "ID_ROUPA": self.listaSelect(query="SELECT id_roupa FROM roupas"),
            "CATEGORIA": self.listaSelect(query="SELECT categoria FROM roupas"),
            "DESCRICAO": self.listaSelect(query="SELECT descricao FROM roupas"),
            "TAMANHO": self.listaSelect(query="SELECT tamanho FROM roupas"),
            "ATIVO": self.listaSelect(query="SELECT ativo FROM roupas"),
            "ID_USER": self.listaSelect(query="SELECT id_user FROM roupas")
        }
    
        return pd.DataFrame(dic)

    @staticmethod
    def imprimirRoupas(self):
        """
            Metodo que imprime:

            1 - Todas as roupas
            2 - Ordenadas por categoria
            3 - Ordenadas por tamanho
        """

        t_roupa = self.roupas(self=Relatorio)

        op = Cadastro.validarInteiro(self=Cadastro, mensagem="Visualizar roupas:\n\n1 - Todas\n2 - Por categoria\n3 - Por tamanho\n")

        roupa = t_roupa.loc[:, ["ID_ROUPA", "CATEGORIA", "DESCRICAO", "TAMANHO"]]

        if (op == 1):
            print("\n-----------------------------------------------\n")
            print(roupa)
            print("\n-----------------------------------------------\n")

        elif(op == 2):
            print("\n-----------------------------------------------\n")
            print(roupa.sort_values(by="CATEGORIA"))
            print("\n-----------------------------------------------\n")
        
        elif (op == 3):
            print("\n-----------------------------------------------\n")
            print(roupa.sort_values(by="TAMANHO"))
            print("\n-----------------------------------------------\n")

    @staticmethod
    def roupasPorNome(self, id_user):
        """ Metodo que imprime roupas que estao ativas por id de usuario """

        dic = {
            "ID": self.listaSelect(query="SELECT id_roupa FROM roupas WHERE id_user = '{:d}'".format(id_user)),
            "CATEGORIA": self.listaSelect(query="SELECT categoria FROM roupas WHERE id_user = '{:d}'".format(id_user)),
            "DESCRICAO": self.listaSelect(query="SELECT descricao FROM roupas WHERE id_user = '{:d}'".format(id_user)),
            "TAMANHO": self.listaSelect(query="SELECT tamanho FROM roupas WHERE id_user = '{:d}'".format(id_user)),
            "ATIVO": self.listaSelect(query="SELECT ativo FROM roupas WHERE id_user = '{:d}'".format(id_user))
        }
    
        t_roupa = pd.DataFrame(dic)
        
        roupa = t_roupa.loc[:, ["ID", "CATEGORIA", "DESCRICAO", "TAMANHO", "ATIVO"]]

        print("\n-----------------------------------------------\n")
        print(roupa)
        print("\n-----------------------------------------------\n")

    """ Estatisticas """ 

    @staticmethod
    def g_roupasPorUsuario(self):

        """ Metodo que imprime e constroi um grafico com quantas roupas cada usuario possui """

        dic = {
            "NOME_USUARIO": self.listaSelect(query="SELECT nome FROM vw_qt_users_roupas"),
            "TOTAL_ROUPAS": self.listaSelect(query="SELECT quantidade FROM vw_qt_users_roupas")
        }

        users_roupas = pd.DataFrame(dic)

        print("\n-----------------------------------------------\n")
        print(users_roupas)
        print("\n-----------------------------------------------\n")
        
        users_roupas.plot(x="NOME_USUARIO", y="TOTAL_ROUPAS")
        plt.figure(figsize=(12, 6))
        plt.show()

        return None

    @staticmethod
    def porcentagens(self):

        """ 
            Metodo que calcula as porcentagens de:

            1 - Roupas por categoria (pelo nome de usuario)
            2 - Roupas por tamanho (pelo nome de usuario)
            3 - Total de roupas desativadas
            4 - Total de usuarios desativados
        """

        def percent(x, total):
            """ Metodo que efetua o calculo da porcentagem """
            return x * 100 / total

        op = Cadastro().validarInteiro(mensagem="Porcentagem:\n\n1 - Roupas por categoria\n2 - Roupas por tamanho\n3 - Roupas desativadas\n4 - Usuarios desativados\n")

        if (op == 1 or op == 2):

            self.imprimirUsuarios(self=Relatorio)
            nome = Cadastro().validarString(mensagem="Digite o nome do usuario desejado: ")

            if (op == 1):

                tot = [ tupla[0] for tupla in Cadastro().executarSelect(query="SELECT SUM(qt_categoria) FROM vw_qt_users_categoria WHERE nome = '{}'".format(nome)) ]
                total = tot[0]

                qt_categoria = [ tupla[0] for tupla in Cadastro().executarSelect(query="SELECT qt_categoria FROM vw_qt_users_categoria WHERE nome = '{}'".format(nome)) ]

                dic = {
                    "CATEGORIA": [ tupla[0] for tupla in Cadastro().executarSelect(query="SELECT categoria FROM vw_qt_users_categoria WHERE nome = '{}'".format(nome)) ],
                    "PORCENTAGEM": [ "{:.1f} %".format(percent(x=num, total=total)) for num in qt_categoria ]
                }

                print("\n-----------------------------------------------\n")
                print(pd.DataFrame(dic))
                print("\n-----------------------------------------------\n")

            elif (op == 2):

                tot = self.listaSelect(query="SELECT SUM(qt_tamanho) FROM vw_qt_users_tamanho WHERE nome = '{}'".format(nome))
                total = tot[0]

                qt_tamanho = self.listaSelect(query="SELECT qt_tamanho FROM vw_qt_users_tamanho WHERE nome = '{}'".format(nome))

                dic = {
                    "TAMANHO": self.listaSelect(query="SELECT tamanho FROM vw_qt_users_tamanho WHERE nome = '{}'".format(nome)),
                    "PORCENTAGEM": [ "{:.1f} %".format(percent(x=num, total=total)) for num in qt_tamanho ]
                }

                print("\n-----------------------------------------------\n")
                print(pd.DataFrame(dic))
                print("\n-----------------------------------------------\n")
        
        elif (op == 3):

            tot = self.listaSelect(query="SELECT COUNT(*) FROM roupas")
            total = tot[0]

            n = self.listaSelect(query="SELECT COUNT(*) FROM roupas WHERE ativo = 0")
            num = n[0]

            print("\n-----------------------------------------------\n")
            print("PORCENTAGEM DE ROUPAS DESATIVADAS: {:.1f} %".format(percent(x=num, total=total)))
            print("\n-----------------------------------------------\n")

        elif (op == 4):

            tot = self.listaSelect(query="SELECT COUNT(*) FROM users")
            total = tot[0]

            n = self.listaSelect(query="SELECT COUNT(*) FROM users WHERE ativo = 0")
            num = n[0]

            print("\n-----------------------------------------------\n")
            print("PORCENTAGEM DE USUARIOS DESATIVADOS: {:.1f} %".format(percent(x=num, total=total)))
            print("\n-----------------------------------------------\n")
