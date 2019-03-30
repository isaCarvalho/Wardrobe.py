"""
Modulo que contem a classe CadastroRoupas.

Esta classe extende a classe Cadastro e possue metodos para:
- Cadastrar uma roupa
- Alterar uma roupa
- Remover uma roupa
- Imprimir todas as roupas

Esta classe esta diretamente ligada ao banco de dados, nao cria objetos do tipo Roupa
"""

from roupas import Roupa
from cadastro import Cadastro
from conexao import Conexao
from cadastroUsuario import CadastroUsuario

class CadastroRoupa(Cadastro):
    """ Classe CadastroRoupa """

    lista_categorias = ['blusa', 'vestido', 'short', 'saia', 'calça', 'casaco', 'jaqueta']
    lista_tamanhos = ['pp', 'p', 'm', 'g', 'gg', 'unico', '36', '38', '40', '42', '44']
    
    @staticmethod
    def cadastrarRoupa(self, id_user):
        """ Metodo que recebe do usuario as caracteristicas da roupa e salva no banco de dados """
        
        categoria = categoria.lower()
        categoria = super().validarCampo(self=Cadastro, lista=self.lista_categorias, mensagem="Digite a categoria: ")    
        
        descricao = super().validarString(self=Cadastro, mensagem="Digite a descricao: ")

        tamanho = tamanho.lower()
        tamanho = super().validarCampo(self=Cadastro, lista=self.lista_tamanhos, mensagem="Digite o tamanho: ")
        
        id_usuario = id_user

        super().executarQuery(self=Cadastro, query="INSERT INTO roupas (categoria, descricao, tamanho, ativo, id_user) VALUES ('{}', '{}', '{}', '{:d}', '{:d}')".format(
            categoria, descricao, tamanho, 1, id_usuario))

    @staticmethod
    def alterarRoupa(self):
        """ Metodo que altera alguma caracteristica da roupa que foi selecionada pelo usuario """

        id_roupa = super().validarInteiro(self=Cadastro, mensagem="Digite o id da roupa a ser pesquisada: ")

        op = super().validarInteiro(self=Cadastro, mensagem="Digite o campo a ser alterado:\n\n1 - Categoria\n2 - Descricao\n3 - Tamanho\n4 - Desativar\n5 - Ativar\n\n")

        if (op == 1):
            categoria = super().validarCampo(self=Cadastro, lista=self.lista_categorias, mensagem="Digite a categoria: ")
            categoria = categoria.lower()

            super().executarQuery(self=Cadastro, query="UPDATE roupas SET categoria = '{}' WHERE id_roupa = {:d}".format(categoria, id_roupa))
        
        elif (op == 2):
            descricao = super().validarString(self=Cadastro, mensagem="Digite a descricao: ")
            
            super().executarQuery(self=Cadastro, query="UPDATE roupas SET descricao = '{}' WHERE id_roupa = {:d}".format(descricao, id_roupa))

        elif (op == 3):
            tamanho = super().validarCampo(self=Cadastro, lista=self.lista_tamanhos, mensagem="Digite o tamanho: ")
            tamanho = tamanho.lower()
            
            super().executarQuery(self=Cadastro, query="UPDATE roupas SET tamanho = '{}' WHERE id_roupa = {:d}".format(tamanho, id_roupa))

        elif (op == 4):
            super().executarQuery(self=Cadastro, query="UPDATE roupas SET ativo = '{:d}' WHERE id_roupa = {:d}".format(0, id_roupa))
        
        elif (op == 5):
            super().executarQuery(self=Cadastro, query="UPDATE roupas SET ativo = '{:d}' WHERE id_roupa = {:d}".format(1, id_roupa))

          
    @staticmethod
    def removerRoupa(self):
        """ Metodo que remove uma roupa do banco de dados"""

        id_roupa = super().validarInteiro(self=Cadastro, mensagem="Digite o id da roupa a ser pesquisada: ")
        
        super().executarQuery(self=Cadastro, query="DELETE FROM roupas WHERE id_roupa = {:d}".format(id_roupa))
