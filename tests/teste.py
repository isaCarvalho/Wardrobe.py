""" Modulo de teste """

from roupas import Roupa
from usuario import Usuario
from cadastroUsuario import CadastroUsuario
from cadastroRoupa import CadastroRoupa
from cadastro import Cadastro

'''
print("\nTESTANDO A ROUPA\n")

roupa = Roupa(id_roupa=1, categoria="blusa", descricao="blusa rosa", tamanho="p")

print("\n----------------------------------\n")
print(roupa)

roupa.setCategoria(categoria="vestido")

print("\n----------------------------------\n")
print(roupa)

roupa.setDescricao(descricao="vestido azul")

print("\n----------------------------------\n")
print(roupa)

roupa.setTamanho(tamanho="unico")

print("\n----------------------------------\n")
print(roupa)

print("\nTESTANDO O USUARIO\n")

usuario = Usuario(id_user=1, nome="Isabela", email="isabelasc@id.uff", senha="password")

print("\n----------------------------------\n")
print(usuario)

usuario.setNome(nome="Isabela Carvalho")

print("\n----------------------------------\n")
print(usuario)

usuario.setEmail(email="isabelasc@id.uff.br")

print("\n----------------------------------\n")
print(usuario)

usuario.setSenha(senha="PASSWORD")

print("\n----------------------------------\n")
print(usuario)

print("\nTESTANDO CADASTRO DE USUARIOS\n")'''

from cadastroUsuario import CadastroUsuario

#CadastroUsuario().cadastrarUsuario(self=CadastroUsuario)

print("\n-------------------------------\n")
#CadastroUsuario().imprimirUsuario(self=CadastroUsuario)

#CadastroUsuario().alterarUsuario(self=CadastroUsuario)

print("\n-------------------------------\n")
#CadastroUsuario().imprimirUsuario(self=CadastroUsuario)


#CadastroUsuario().removerUsuario(self=CadastroUsuario)


CadastroUsuario().imprimirUsuario(self=CadastroUsuario)

print("\n-------------------------------\n")
#print("\nTESTANDO CADASTRO ROUPA\n")


#CadastroRoupa().cadastrarRoupa(self=CadastroRoupa)
CadastroRoupa().imprimirRoupa(self=CadastroRoupa)


print("\n-------------------------------\n")
#CadastroRoupa().alterarRoupa(self=CadastroRoupa)
#CadastroRoupa().imprimirRoupa(self=CadastroRoupa)

#print("\n-------------------------------\n")
#CadastroRoupa().removerRoupa(self=CadastroRoupa)

#print("\n-------------------------------\n")
#CadastroRoupa().imprimirRoupa(self=CadastroRoupa)


from relatorio import Relatorio

Relatorio()

Relatorio.imprimirRoupasAtivas(self=Relatorio)
print(Relatorio.lista_id_users)
print(Relatorio.set_id_users)
print(Relatorio.dicionario(self=Relatorio))

print("\n")
Relatorio.imprimirRoupasPorUsuario(self=Relatorio)