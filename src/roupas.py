"""
Modulo que contem a classe Roupas.

Esta classe possui os atributos dos objetos do tipo Roupa e metodos setters e getters
Esta classe nao esta sendo usada, mas foi implementada para uma possivel adaptacao do programa
"""

class Roupa():
    """ Classe Roupa """

    id_roupa = None
    categoria = None
    descricao = None
    tamanho = None
    ativo = None
    id_usuario = None

    def __init__(self, id_roupa, categoria, descricao, tamanho, ativo, id_usuario):
        """ Metodo construtor da classe Roupa """

        self.id_roupa = id_roupa
        self.categoria = categoria
        self.descricao = descricao
        self.tamanho = tamanho
        self.ativo = ativo
        self.id_usuario = id_usuario

    def setId(self, id_roupa):
        self.id_roupa = id_roupa
    
    def getId(self):
        return self.id_roupa

    def setCategoria(self, categoria):
        self.categoria = categoria

    def getCategoria(self):
        return self.categoria

    def setDescricao(self, descricao):
        self.descricao = descricao
    
    def getDescricao(self):
        return self.descricao

    def setTamanho(self, tamanho):
        self.tamanho = tamanho
    
    def getTamanho(self):
        return self.tamanho

    def setAtivo(self, ativo):
        self.ativo = ativo

    def getAtivo(self):
        return self.ativo

    def setIdUsuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getIdUsuario(self):
        return self.id_usuario

    def __str__(self):
        return "ID: {:d}\nCATEGORIA: {}\nDESCRICAO: {}\nTAMANHO: {}\nATIVO: {}\nID_USUARIO: {:d}\n".format(
            self.id_roupa, 
            self.categoria, 
            self.descricao, 
            self.tamanho, 
            self.ativo, 
            self.id_usuario
            )