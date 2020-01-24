# Programa feito por:
# Paulo Virgilio
# Francisco Faria

# todos os importes feitos
from album import albums
from artist import artists
from genre import genres
from music import musics
from view import views
from db import db

#instancias
db = db()
album = albums()
artist = artists()
genre = genres()
music = musics()
view = views()


class menu: # classe menu que contem todas as funcoes a executar do programa
    def __init__(self, resp=None, resp1=None, resp2=None, resp3=None, resp4=None):
        self.resp =  resp
        self.resp1 = resp1
        self.resp2 = resp2
        self.resp3 = resp3
        self.resp4 = resp4

    def menu_inicio(self): # funcao menu que sera apresentado
        view.introducao()
        while self.resp != 5: # verifica a resposta do utilizador ate ser diferente de 5
            view.base()
            self.resp = input ( "\nEscolha uma opcao: " )

            if self.resp == '1': # se for 1 avanca para listar dados
                view.escolha_tabela() # view para escolher tabela
                self.resp1 = input ( "\nSelecione uma opcao:" )
                self.escolher_listar_tabela()

            elif self.resp == '2': # se for 2 avanca para inserir dados
                view.escolha_tabela() # view para escolher tabela
                self.resp2 = input ( "\nSelecione uma opcao:" )
                self.escolher_dados_tabela()

            elif self.resp == "3": # se for 3 avanca para apagar dados
                view.escolha_tabela() # view para escolher tabela
                self.resp3 = input ( "\nSelecione uma opcao:" )
                self.apagar_dados_tabela()

            elif self.resp == "4": # se for 4 avanca para alterar dados
                view.escolha_tabela() # view para escolher tabela
                self.resp4 = input ( "\nSelecione uma opcao:" )
                self.alterar_dados_tabela()

            elif self.resp == '5': # se for 5 sai do programa
                print ( "\nA Sair do Programa! Obrigado! Ate-breve!")
                quit()

            else: # escolha diferente da erro
                print ( "\n ESCOLHA UMA OPCAO VALIDA!" )

    def escolher_listar_tabela(self):
        if self.resp1 == '1': # se for 1 lista os albums
            album.show_albums() # executa a funcao de listar albums

        elif self.resp1 == '2': # se for 2 lista os artistas
            artist.show_artists() # executa a funcao de listar artistas

        elif self.resp1 == '3': # se for 3 lista os generos
            genre.show_genres() # executa a funcao de listar generos

        elif self.resp1 == '4': # se for 4 lista as musicas
            music.show_musics() # executa a funcao de listar musicas

        elif self.resp4 == '5': # se for 5 volta atras
            self.menu_inicio() # volta para menu inicial

        elif self.resp4 == '6': # se for 6 sai do programa
            print ( "\nA Sair do Programa! Obrigado! Ate-breve!" )
            quit()

        else: # outra opcao diferente da erro
            print ( "\nESCOLHA UMA OPCAO VALIDA!" )

    def escolher_dados_tabela(self):
        if self.resp2 == '1': # se for 1 insere novos albums
            album.inserir_albums() # executa a funcao de inserir albums

        elif self.resp2 == '2': # se for 2 insere novos artistas
            artist.inserir_artist() # executa a funcao de inserir artistas

        elif self.resp2 == '3': # se for 3 insere novos generos
            genre.inserir_genres() # executa a funcao de inserir generos

        elif self.resp2 == '4': # se for 4 insere novas musicas
            music.inserir_musics() # executa a funcao de inserir musicas

        elif self.resp4 == '5': # se for 5 volta atras
                self.menu_inicio() # volta para menu inicial

        elif self.resp4 == '6': # se for 6 sai do programa
            print ( "\nA Sair do Programa! Obrigado! Ate-breve!" )
            quit()
        else: # outra opcao diferente da erro
            print ( "\n ESCOLHA UMA OPCAO VALIDA!" )

    def apagar_dados_tabela(self):
        if self.resp3 == '1': # se for 1 apaga albums
            album.apagar_albums() # executa a funcao de apagar albums

        elif self.resp3 == '2': # se for 2 apaga artistas
            artist.apagar_artist() # executa a funcao de apagar artistas

        elif self.resp3 == '3': # se for 3 apaga generos
            genre.apagar_genres() # executa a funcao de apagar generos

        elif self.resp3 == '4': # se for 4 apaga musicas
            music.apagar_musics() # executa a funcao de apagar musicas

        elif self.resp4 == '5': # se for 5 volta atras
            self.menu_inicio() # volta para menu inicial

        elif self.resp4 == '6': # se for 6 sai do programa
            print ( "\nA Sair do Programa! Obrigado! Ate-breve!" )
            quit()

        else: # outra opcao diferente da erro
            print ( "\nESCOLHA UMA OPCAO VALIDA!" )

    def alterar_dados_tabela(self):
        if self.resp4 == '1': # se for 1 altera dados dos albums
            album.alterar_albums() # executa a funcao de alterar albums

        elif self.resp4 == '2': # se for 2 altera dados dos artistas
            artist.alterar_artists() # executa a funcao de alterar artistas

        elif self.resp4 == '3': # se for 3 altera dados dos generos
            genre.alterar_genres() # executa a funcao de alterar generos

        elif self.resp4 == '4': # se for 4 altera dados das musicas
            music.alterar_musics() # executa a funcao de alterar musicas

        elif self.resp4 == '5': # se for 5 volta atras
            self.menu_inicio() # volta para menu inicial

        elif self.resp4 == '6': # se for 6 sai do programa
            print ( "\nA Sair do Programa! Obrigado! Ate-breve!" )
            quit()

        else:# outra opcao diferente da erro
            print ( "\nESCOLHA UMA OPCAO VALIDA!" )


# instancia para executar menu
comeco = menu()
comeco.menu_inicio()