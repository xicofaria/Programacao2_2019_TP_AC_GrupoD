# importes dos ficheiros views e db
import sqlite3
from db import db
from view import views

# instancias
db = db()
view = views()


class albums(): # classe para os albums

    def __init__( self, albumid=None, title=None, artistid=None, results=None ):
        self.albumid =  albumid
        self.title =    title
        self.artistid = artistid
        self.results =  results

    def show_albums(self): # Funcao para listar os albums
        db.__init__()
        pergunta = input ( "\n1.Listar TODOS os Albums | 2.Listar POR LETRA/NOME os Albums:" )
        # Uma pergunta feita para saber se pretende listar tudo ou por nome/letra

        if pergunta == '1': # se escolher todas os albums
            db.cursor.execute ( "select * from albums limit 00,1000;" )
            self.results = db.cursor.fetchall()
            view.apresentacao_dados_albums()  # view para ver como os dados do album sao apresentados

            for i, row in enumerate ( self.results, start=1 ): # vai numerar os resultados do album a começar do 1
                print ( row )

                if i % 20 == 0: # if para apenas mostrar 20 albums de cada vez e enter para listar mais
                    x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!:" )

                    if x == '':
                        continue

                    elif x == 'S' or x == 's':
                        break

                    elif x != 'S' or x == 's':
                        print ( "\nOPCAO INVALIDA!\n" )
                        break

        elif pergunta == '2': # opcao de listar por letra/nome
            askLetter = input ( "\nListar todos os 'Albums' pela letra:" )
            db.cursor.execute ( "Select * FROM albums WHERE Title like'" + askLetter + "%'" )
            self.results = db.cursor.fetchall()
            view.apresentacao_dados_albums()

            for i, row in enumerate ( self.results, start=1 ): # vai numerar os resultados do album a começar do 1
                print ( row )

                if i % 10 == 0: # if para apenas mostrar 10 albums de cada vez e enter para listar mais
                    x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!:" )

                    if x == '':
                        continue

                    elif x == 'S' or x == 's':
                        break

                    elif x != 'S' or x == 's':
                        print ( "\nOPCAO INVALIDA!\n" )
                        break
        else: # uma opcao diferente das disponiveis
            print ( "\nESCOLHA UMA OPCAO VALIDA!\n" )

    def inserir_albums(self): # Funcao para inserir novos albums
        db.__init__()
        print ( "\nEsta prestes a INSERIR dados na tabela 'Albums'." )

        while True: # ciclo while para pedir informacoes do album ao utilizador
            try:
                self.title =    input ( "\nTitulo do album: " )
                self.artistid = int ( input ( "ID do artista: " ) )

                if self.title == '' or self.title == ' ': # titulo vazio da erro
                    print ( "\nERRO! INSIRA TODOS OS DADOS!" )
                    break

                elif self.artistid == '' or self.artistid == ' ': # id do artista da erro
                    print ( "\nERRO! INSIRA TODOS OS DADOS!" )
                    break

                else: # continua senao houver erros nenhums
                    try:
                        with db.connection:
                            db.cursor.execute ( '''SELECT Title FROM albums WHERE Title=?''', ( self.title, ) )
                            exists = db.cursor.fetchall()

                            if not exists: # vai verificar o nome do album na bd senao existir executa
                                db.cursor.execute ( '''INSERT INTO albums(Title, Artistid) VALUES(?,?)''', ( self.title, self.artistid ) )
                                db.getcommit()
                                print ( "\nDados inseridos com sucesso na tabela 'Albums' da base de dados." )
                                print ( "\nTitulo:", self.title )
                                print ( "ID Artista:", self.artistid )
                                break

                            else: # senao da erro que o nome do album ja existe na bd
                                print ( "\nERRO! O Album com o Titulo,",self.title,"ja existe!" )

                    except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
                        print ( "\nERRO! Impossivel criar Album!" )

                    finally:
                        db.closedb()

            except ValueError as error: # qualquer outro erro de parametros
                print("\nErro de Parametro! Valor Inteiro/Decimal/Vazio!")
                print("Erro:", error)
                break

    def apagar_albums(self): # Funcao para apagar albums
        db.__init__()
        print ( "\nEsta prestes a APAGAR dados da tabela 'Albums'." )
        self.title = input ( "Titulo do Album: " )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Title FROM albums WHERE Title=?''', ( self.title, ) )
                exists = db.cursor.fetchall()

                if exists: # se o nome do album existir na bd continua e apaga
                    db.cursor.execute ( '''DELETE FROM Albums WHERE Title = ? ''', ( self.title, ) )
                    db.getcommit()
                    print ( "\nO Album", self.title,"foi eliminado com sucesso!" )

                else: # senao da erro
                    print ( "\nERRO! O Album", self.title,"nao existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel APAGAR o album!" )

        finally:
            db.closedb()

    def alterar_albums(self): # Funcao para modificar os dados de cada album
        db.__init__()
        print ( "\nEsta prestes a ALTERAR dados da tabela 'Albums'." )
        alt1 = input ( "\nPretende alterar: 1.TITULO | 2.ID do Artista: " )

        try:
            with db.connection:

                if alt1 == '1': # a escolha um para alterar o titulo do album
                    self.title = input ( "\nInsira o Titulo do album que pretende alterar: " )
                    db.cursor.execute ( '''SELECT Title FROM albums WHERE Title = ? ''', ( self.title, ) )
                    exists1 = db.cursor.fetchall()

                    if exists1: # se existir o titulo do album pode colocar o novo titulo
                        new_title = input ( "Insira o NOVO Titulo do album: " )
                        db.cursor.execute ('''SELECT Title FROM albums WHERE Title = ? ''', ( new_title, ) )
                        exists = db.cursor.fetchall()

                        if not exists: # se nao existir o novo titulo na bd e alterado
                            db.cursor.execute ( '''UPDATE albums SET Title = ? WHERE Title = ? ''', ( new_title, self.title ) )
                            db.getcommit()
                            print ( "\nO Titulo do Album foi alterado com sucesso!" )
                            print ( "O Album",self.title,"possui um novo Titulo:", new_title )

                        else: # se o novo titulo ja existe da erro
                            print ( "\nERRO! O Album",new_title,"ja existe!" )

                    else: # se o album nao existir na bd
                        print ( "\nERRO! O Album",self.title,"nao existe!" )

                elif alt1 == '2': # se escolher a operacao de mudar id do artista
                    self.title = input ( "\nInsira o Titulo do album que pretende alterar o ID do Artista: " )
                    db.cursor.execute('''SELECT Title FROM albums WHERE Title = ? ''', (self.title,))
                    exists = db.cursor.fetchall() # guarda o titulo do album para ver se existe na bd

                    if exists: # se existir pode continuar
                        new_artistid = input ( "Insira o NOVO ID do artista: " )
                        db.cursor.execute ( '''UPDATE Albums SET ArtistId = ? WHERE Title = ? ''', ( new_artistid, self.title ) )
                        db.getcommit()
                        print ( "\nID do Artista alterado com sucesso!" )
                        print ( "O Album",self.title,"possui um novo Artista com o ID:", new_artistid )

                    else: # senao existir da erro
                        print ( "\nERRO! O Album nao existe!" )

                else: # caso escolha uma outro opcao da erro
                    print ( "\nEscolha uma opcao valida!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel ALTERAR o Album!")

        finally:
            db.closedb()


