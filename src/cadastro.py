"""
Modulo que contem a classe Cadastro.

Esta classe contem metodos para tratamentos de erros, validacao de dados e execucao de queries
"""

from conexao import Conexao

class Cadastro(object):
    """ Classe Cadastro """

    def mensagemDeErro(erro):
        """ Metodo que imprime uma mensagem de erro e seu tipo """
        print("Erro do tipo {}: {}\n".format(type(erro), erro))

    def executarQuery(self, query=""):
        """ Metodo que executa uma query que ira modificar o banco de dados e trata possiveis erros """
        try:

            cnx = Conexao.abrirConexao(self=Conexao)
            myCursor = cnx.cursor()

            myCursor.execute(query)
            cnx.commit()

            cnx.close()

        except Exception as erro:

            self.mensagemDeErro(erro=erro)

    def executarSelect(self, query=""):
        """ Metodo que executa um select e retorna todos os seus registros """
        try:
            cnx = Conexao.abrirConexao(self=Conexao)
            myCursor = cnx.cursor()

            myCursor.execute(query)
            tabela = myCursor.fetchall()

            cnx.close()

            return tabela
        except Exception as erro:

            self.mensagemDeErro(erro=erro)

    def validarInteiro(self, mensagem):
        """ Metodo que valida um numero inteiro e trata possiveis erros """
        while (True):
            try:
                op = int(input(mensagem))
                return op
            except Exception as erro:
                self.mensagemDeErro(erro=erro)

    def validarString(self, mensagem):
        """ Metodo que valida uma string """
        while(True):
            try:
                dado = input(mensagem)
                return dado
            except Exception as erro:
                self.mensagemDeErro(erro=erro)

    def isValid(dado, lista):
        """ Metodo que procura se um dado esta em uma lista - usado para procurar tamanhos e categorias """
        if dado in lista:
            return True
        return False

    def validarCampo(self, lista, mensagem):
        """ Metodo que valida um campo - valida tamanhos e categorias """

        while (True):
            campo = self.validarString(self=Cadastro, mensagem=mensagem)
            if (self.isValid(dado=campo, lista=lista)):
                break
            print("\nDado invalido!\n")
        
        return campo
