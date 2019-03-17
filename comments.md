# Comentários gerais do sistema

=======================================================

## Organização de diretórios

- O diretório 'dumps' guarda os dumps do banco de dados;
- O diretório 'tests' guarda os testes realizados com algumas bibliotecas;
- O diretório 'src' guarda todo o código fonte do programa;
- O diretório 'graphics' guarda os gráficos gerados pelos relatórios do programa

=======================================================

## Organização do código fonte

O código fonte está divido nas seguintes classes:

1. Conexao
2. Cadastro
3. CadastroRoupa
4. CadastroUsuario
5. Relatorio
6. MenuRoupa
7. MenuUsuario
8. Roupa
9. Usuario

e pelo módulo princiapal que contém a função main (main.py)

### 1. Conexao:

É a classe que faz a conexão com o banco de dados, a partir do conector do MySQL. Esta classe trata os devidos erros relacionados à conexão com o banco de dados;

### 2. Cadastro:

Esta classe herda da classe conexão e possui função de execução de queries, tratamento de demais erros e validação de dados.

### 3. CadastroRoupa:

Esta classe herda da classe cadastro, e possui funções para a manipulação de dados da tabela 'roupas' do banco de dados.

### 4. CadastroUsuario:

Esta classe também herda da classe cadastro, e possui funções para a manipulação de dados da tabela 'users' do banco de dados.

### 5. Relatorio:

Esta classe implementa funções para estatísticas e consulta de dados gerais e de um usuário específico.

### 6. MenuRoupa:

Esta classe implementa o menu com as opções relacionadas a roupa

### 7. MenuUsuario:

Esta classe implementa o menu com as opções relacionadas a usuários

### Módulo Principal main.py:

Módulo que possui a função main(). Esta por sua vez, chama os menus de usuarios e implementa o menu de relatórios.

=======================================================

## Demais observações

1. As classes 8.Roupa e 9.Usuario estão implementadas para uma possível modificação;

2. Posteriormente, implementações de interfaces gráficas estão sendo cogitadas.
