"""
Modulo que contem a classe Usuario.

Esta classe possui os atributos dos objetos do tipo Usuario e metodos setters e getters
Esta classe nao esta sendo usada, mas foi implementada para uma possivel adaptacao do programa
"""

class Usuario():
    """ Classe Usuario """

    id_user = None
    nome = None
    email = None
    senha = None
    ativo = None

    def __init__(self, id_user, nome, email, senha, ativo):
        """ Metodo construtor da classe Usuario """
        self.id_user = id_user
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

    def setId(self, id_user):
        self.id_user = id_user

    def getId(self):
        return self.id_user

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setSenha(self, senha):
        self.senha = senha

    def getSenha(self):
        return self.senha

    def setAtivo(self, ativo):
        self.ativo = ativo

    def getAtivo(self):
        return self.ativo

    def __str__(self):
        return "ID: {:d}\nNOME: {}\nEMAIL: {}\nSENHA: {}".format(
            self.id_user, 
            self.nome, 
            self.email, 
            self.senha)