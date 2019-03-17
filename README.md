# WARDROBE.PY

O objetivo do programa é ser um guarda-roupa automatizado, de forma que o usuario poderá ter organizador sem precisar abrir seu guarda-roupa físico. O programa também conta com relatorios completos desde quantas roupas foram não estão mais em bom estado, ou seja, quantas foram desativadas (por todos os usuarios e somente por ele), até o gráfico de roupas por usuarios. 

Linguagem: Python 3
Banco de Dados: MySQL 5.0.12

## PRÉ-REQUISITOS

Versão 3 ou superior do Python;

## AUTORES

- Isabela Silva de Carvalho

## LINKS

GitHub: https://github.com/isaCarvalho/projeto_python

## FUNCIONALIDADES

### MENU PRINCIPAL

O menu principal eh composto de duas opcoes:

1. Menu Usuario
2. Relatorios
3. Sair


#### 1.1 MENU USUARIO 1

- A primeira opcao do menu principal leva ao menu de usuario, apenas com as opcoes:

1. Entrar
2. Cadastrar
3. Sair

- Opção 2: o usuario ira digitar seus dados cadastrais e podera logar assim que estiver cadastrado;

#### 1.2 MENU USUARIO 2

- Na primeira opcao do menu de usuario, o usuario irá logar no sistema. Apenas com ele logado conseguira ir para o menu de roupas e demais opcoes do menu de usuario, que são:

1. Alterar dados
2. Menu roupas
3. Sair

- Opção 1: o usuario ira selecionar o dado a ser alterado e logo depois voltará ao menu principal

#### 1.3 MENU ROUPAS

No menu roupas estarão todas as opcoes relacionadas a roupa

1. Cadastrar Roupa
2. Minhas roupas
3. Alterar Roupa
4. Excluir permanentemente
5. Sair

- Opcao 1: O usuario digitará os dados cadastrais da roupa que ele deseja incluir
- Opcao 2: Serão impressas todas as roupas pertencentes ao usuario logado no momento
- Opção 3: O usuario selecionará qual campo ele deseja alterar, e logo após a alteração, voltará ao menu roupas
- Opção 4: Exclui uma roupa permanentemente, ou seja, exclui o registro da roupa no banco de dados

### O USUARIO NAO PRECISA ESTAR LOGADO PARA UTILIZAR AS OPÇÕES DE RELATÓRIOS

#### 2.1 MENU RELATORIO 1

1. Visualizar
2. Estatisticas

#### 2.2 VISUALIZAR

Imprime todos os usuarios (identificador, nome, email) ordenados por nome

Logo em seguida, o usuario selecionará como ele deseja visualizar as roupas:

1. Todas
2. Por categoria
3. Por tamanho

- Opção 1: imprimirá na tela todas as roupas, sem filtros
- Opção 2: imprimirá na tela todas as roupas ordenadas por categoria
- Opção 3: imprimirá na tela todas as roupas ordenadas por tamanho

Após o modo de visualização ser selecionado, o programa voltará ao menu principal

#### 2.3 ESTATISTICAS

1. Grafico de roupas por usuarios
2. Porcentagens

- Opção 1: Será gerado um gráfico da quantidade de roupas por usuario em formato ".png".
OBS: Este gráfico deverá ser salvo na pasta "graphics"

#### 2.4 PORCENTAGENS

1. Roupas por categoria
2. Roupas por tamanho
3. Roupas desativadas
4. Usuarios desativados

- Opção 1: Mostrará a porcentagem de roupas de acordo com uma categoria.
Deverá ser informado o nome de usuario, e o programa mostrará os percentuais de cada categoria de roupas que aquele usuario possui.
Logo após, o programa voltará ao menu principal

- Opção 2: Mostrará a porcentagem de roupas de acordo com um tamanho.
Deverá ser informado o nome do usuario, e o programa mostrará os percentuais de cada tamanho de roupas que aquele usuario possui.
Logo após, o programa voltará ao menu principal

- Opção 3: Mostrará a porcentagem de roupas que foram desativadas, independente do usuario. Logo após, o programa voltará ao menu principal.

- Opção 4: Mostrará a porcentagem de usuarios desativados. Logo após, o programa voltará ao menu principal.

### LIMITAÇÕES

**O programa não gera combinações de peças de roupas.**
