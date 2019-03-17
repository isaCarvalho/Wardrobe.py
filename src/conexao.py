""" 
Modulo que contem a classe Conexao.

Esta classe eh a que abre a conexao com o banco de dados e trata os devidos erros 
"""

import mysql.connector
from mysql.connector import errorcode

class Conexao():
    """ Classe Conexao """

    cnx = None

    @staticmethod
    def abrirConexao(self):
        """ Metodo que abre a conexao com o banco de dados passando o usuario e a base de dados e trata possiveis erros """ 

        try:

            self.cnx = mysql.connector.connect(user='root', database='wardrobe_py')
            return self.cnx

        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Nome de usuario ou senha incorretos")

            elif erro.errno == errorcode.ER_BAD_DB_ERROR:
                print("A base de dados nao existe")
            else:
                print("Erro do tipo {}: {}".format(type(erro), erro))

            exit()

        else:
            self.cnx.close()
            return 0