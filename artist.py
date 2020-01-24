# importes dos ficheiros views e db
import sqlite3
from db import db
from view import views

# instancias
view = views()
db = db()


class artists(): # Classe dos artistas

    def __init__(self, artistID=None, name=None, results=None):
        self.artistID = artistID
        self.name =     name
        self.results =  results

    def show_artists(self): # Funcao para listar artistas
        db.__init__()
        pergunta = input ( "\n1.Listar TODOS os Artistas | 2.Listar POR LETRA/NOME os Artistas:" )
        # Uma pergunta feita para saber se pretende listar tudo ou por nome/letra

        if pergunta == '1': # se escolher todos os artistas
            view.apresentacao_dados_artistas() # view para ver como os dados do artista sao apresentados
            db.cursor.execute ( "select * from artists limit 00,1000;" )
            self.results = db.cursor.fetchall()

            for i, row in enumerate ( self.results, start=1 ): # vai numerar os resultados do artista a começar do 1
                print ( row )

                if i % 20 == 0: # if para apenas mostrar 20 artistas de cada vez e enter para listar mais
                    x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!:" )

                    if x == '':
                        continue

                    elif x == 'S' or x == 's':
                        break

                    elif x != 'S' or x == 's':
                        print ( "\nOPCAO INVALIDA!\n" )
                        break

        elif pergunta == '2': # opcao de listar por letra/nome
            askLetter = input ( "\nListar todos os 'Artistas' pela LETRA/NOME: " )
            db.cursor.execute ( "Select * FROM artists WHERE Name like'" + askLetter + "%'" )
            self.results = db.cursor.fetchall()
            view.apresentacao_dados_artistas() # view para ver como os dados do artista sao apresentados

            for i, row in enumerate ( self.results, start=1 ):  # vai numerar os resultados do artista a começar do 1
                print ( row )

                if i % 10 == 0: # if para apenas mostrar 10 artistas de cada vez e enter para listar mais
                    x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!: " )

                    if x == '':
                        continue

                    elif x == 'S' or x == 's':
                        break

                    elif x != 'S' or x == 's':
                        print ( "\nOPCAO INVALIDA!\n" )
                        break

        else: # uma opcao diferente das disponiveis
            print ( "\nESCOLHA UMA OPCAO VALIDA!\n" )

    def inserir_artist(self): # Funcao para inserir novos artistas
        db.__init__() 
        print ( "\nEsta prestes a INSERIR dados na tabela 'ARTISTAS'." )
        self.name = input ( "Nome do artista: " )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM artists WHERE Name=?''', ( self.name, ) )
                exists = db.cursor.fetchall()

                if not exists: # se o artista nao existir ja na bd executa
                    db.cursor.execute ( '''INSERT INTO artists(Name) VALUES(?)''', ( self.name, ) )
                    db.getcommit()
                    print ( "\nDados inseridos com sucesso na tabela 'Artistas' da base de dados." )
                    print ( "Artista:", self.name )

                else: # se o novo nome ja existe da erro
                    print ( "\nERRO! O Artista",self.name,"ja existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel inserir Artista!" )

        finally:
            db.closedb()

    def apagar_artist(self): # Funcao para apagar artistas
        db.__init__()
        print ( "\nEsta prestes a APAGAR dados da tabela 'ARTISTAS'." )
        self.name = input ( "Nome do Artista:" )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM artists WHERE Name=?''', ( self.name, ) )
                exists = db.cursor.fetchall()

                if exists: # se o nome do artista existir na bd continua e apaga
                    db.cursor.execute ( '''DELETE FROM artists WHERE Name = ? ''', ( self.name, ) )
                    db.getcommit()
                    print ( "\nO Artista,",self.name,"foi eliminado com sucesso!" )

                else: # senao da erro
                    print ( "\nERRO! O Artista",self.name,"nao existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel APAGAR o Artista!" )

        finally:
            db.closedb()

    def alterar_artists(self): # Funcao para alterar os dados de cada artista
        db.__init__()
        print ( "\nEsta prestes a ALTERAR dados da tabela 'ARTISTAS'." )
        self.name = input ( "\nInsira o NOME do Artista que pretende Alterar: " )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM artists WHERE Name = ? ''', ( self.name, ) )
                exists1 = db.cursor.fetchall()

                if exists1: # se existir o nome do artista pode colocar o novo nome
                    new_name = input ( "Insira o novo NOME do Artista: " )
                    db.cursor.execute ( '''SELECT Name FROM artists WHERE Name = ? ''', ( new_name, ) )
                    exists = db.cursor.fetchall()

                    if not exists: # se nao existir o novo nome na bd e alterado
                        db.cursor.execute ( '''UPDATE artists SET Name = ? WHERE Name = ? ''', ( new_name, self.name ) )
                        db.getcommit()
                        print ( "\nO Nome do Artista foi alterado com sucesso!" )
                        print ( "O Artista", self.name, "possui um novo Nome:", new_name )

                    else: # se o novo nome ja existe da erro
                        print ( "\nERRO! O Artista",new_name,"ja existe!" )

                else: # se o artista nao existir na bd
                    print ( "\nERRO! O Artista",self.name,"nao existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel ALTERAR o Artista!" )

        finally:
            db.closedb()

