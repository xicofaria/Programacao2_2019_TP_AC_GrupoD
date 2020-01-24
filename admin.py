from db import db
from album import albums
from music import musics
import sys

a = albums()
m = musics()

# Menu das operações
def menuop():
    print ( "")
    print ( "|     MENU ADMIN    |" )
    print ( "")
    print ( "  1. Listar         " )
    print ( "  2. Inserir        " )
    print ( "  3. Modificar      " )
    print ( "  4. Eliminar       " )
    print ( "  5. Sair           " )
    print ( "\n")


# Menu das Tabelas
def menutab():
    print ( "      TABELAS      " )
    print ( "  1) Albums        " )
    print ( "  2) Musicas        " )
    print ( "\n" )


# Apresentar o menu até que seja premida a opção de sair
while True:
    menuop()
    # Escolha da operação
    op = input ( "Escolha uma opcao do Menu: " )

    # Opção de listar
    if op == "1":
        menutab()
        # Escolha da tabela
        tabela = input ( "Em qual tabela deseja fazer a operação? " )
        # Se for escolhida a tabela Albums

        if tabela == "1":
            a.show_albums()
        # Se for escolhida a tabela Musics

        if tabela == "2":
            m.show_musics()


    # opção inserir
    if op == "2":
        menutab()
        tabela = input ( "Em qual tabela deseja fazer a operação? " )

        if tabela == "1":
            a.inserir_albums()

        if tabela == "2":
            m.inserir_musics()

    # opção modificar
    if op == "3":
        menutab()
        tabela = input ( "Em qual tabela deseja fazer a operação? " )

        if tabela == "1":
            a.alterar_albums()

        if tabela == "2":
            m.alterar_musics()

    # opção eliminar
    if op == "4":
        menutab()
        tabela = input ( "Em qual tabela deseja fazer a operação? " )

        if tabela == "1":
            a.apagar_albums()

        if tabela == "2":
            m.apagar_musics()

    # opção sair
    if op == "5":
        sys.exit()

