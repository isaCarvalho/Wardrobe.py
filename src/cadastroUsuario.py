"""
Modulo que contem a classe CadastroUsuario.

Esta classe extende a classe Cadastro e possue metodos para:
- Cadastrar um usuario
- Alterar um usuario
- Remover um usuario
- Imprimir todos os usuarios

Esta classe esta diretamente ligada ao banco de dados, nao cria objetos do tipo Usuario
"""

from getpass import getpass
from usuario import Usuario
from cadastro import Cadastro
from conexao import Conexao

class CadastroUsuario(Cadastro):
    """ Classe CadastroUsuario """

    @staticmethod
    def cadastrarUsuario(self):
        """ Metodo estatico para cadastrar um usuario diretamente no banco de dados """

        nome = super().validarString(self=Cadastro, mensagem="Digite seu nome: ")

        email = super().validarString(self=Cadastro, mensagem="Digite seu email: ")

        senha = getpass("Digite sua senha: ") 

        super().executarQuery(self=Cadastro, query="INSERT INTO users (nome, email, senha, ativo) VALUES ('{}', '{}', '{}', '{:d}')".format(nome,email,senha,1))   

    @staticmethod
    def alterarUsuario(self, id_usuario):
        """ Metodo estatico para alterar algum campo de um usuario """

        id_user = id_usuario

        op = super().validarInteiro(self=Cadastro, mensagem="Digite o campo a ser alterado:\n\n1 - Nome\n2 - Email\n3 - Senha\n4 - Desativar\n5 - Ativar\n\n")

        if (op == 1):
            nome =  super().validarString(self=Cadastro, mensagem="Digite o nome: ")
            
            super().executarQuery(self=Cadastro, query="UPDATE users SET nome = '{}' WHERE id_user = {:d}".format(nome, id_user))

        elif (op == 2):
            email = super().validarString(self=Cadastro, mensagem="Digite o email: ")

            super().executarQuery(self=Cadastro, query="UPDATE users SET email = '{}' WHERE id_user = {:d}".format(email, id_user))

        elif (op == 3):
            senha = getpass("Digite a senha: ")

            super().executarQuery(self=Cadastro, query="UPDATE users SET senha = '{}' WHERE id_user = {:d}".format(senha, id_user))

        elif (op == 4):
            super().executarQuery(self=Cadastro, query="UPDATE users SET ativo = '{:d}' WHERE id_user = {:d}".format(0, id_user))
            
        elif (op == 5):
            super().executarQuery(self=Cadastro, query="UPDATE users SET ativo = '{:d}' WHERE id_user = {:d}".format(1, id_user))

    @staticmethod
    def removerUsuario(self, id_usuario):
        """ Metodo estatico para remover um usuario do banco de dados. """

        id_user = id_usuario
        
        super().executarQuery(self=Cadastro, query="DELETE FROM users WHERE id_user = {:d}".format(id_user))