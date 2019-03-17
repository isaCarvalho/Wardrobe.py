from conexao import Conexao
from cadastro import Cadastro

import pandas as pd

class TestePandas():

    cnx = Conexao.abrirConexao(self=Conexao)

    @staticmethod
    def Usuarios():
        nomes = Cadastro.executarSelect(self=Cadastro, query="SELECT nome FROM users")
        emails = Cadastro.executarSelect(self=Cadastro, query="SELECT email FROM users")
        senhas = Cadastro.executarSelect(self=Cadastro, query="SELECT senhas FROM users")
        ativos = Cadastro.executarSelect(self=Cadastro, query="SELECT ativo FROM users")

        dic = {
            "nome": [ nome for nome in nomes ],
            "email": [ email for email in emails ],
            "senha": [ senha for senha in senhas ],
            "ativo": [ ativo for ativo in ativos ] 
        } 

        usuarios = pd.DataFrame(dic)

        print(usuarios)

TestePandas().Usuarios()
