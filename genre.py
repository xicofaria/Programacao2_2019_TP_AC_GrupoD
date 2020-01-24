# importes dos ficheiros views e db
import sqlite3
from db import db
from view import views

# instancias
db = db()
view = views()


class genres(): # Classe dos generos

    def __init__(self, genreId=None, name=None, results=None):
        self.genreId = genreId
        self.name =    name
        self.results = results

    def show_genres(self): # Funcao para listar generos
        db.__init__()
        pergunta = input ( "\n1.Listar TODOS os Generos | 2.Listar POR LETRA/NOME os Generos:" )
        # Uma pergunta feita para saber se pretende listar tudo ou por nome/letra

        if pergunta == '1': # se escolher todos os generos
            view.apresentacao_dados_generos() # view para ver como os dados do genero sao apresentados
            db.cursor.execute ( "select * from genres limit 00,1000;" )
            self.results = db.cursor.fetchall()

            for i, row in enumerate( self.results, start=1 ): # vai numerar os resultados do genero a começar do 1
                print ( row )

                if i % 20 == 0: # if para apenas mostrar 20 genros de cada vez e enter para listar mais
                    x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!:" )

                    if x == '':
                        continue

                    elif x == 'S' or x == 's':
                        break

                    elif x != 'S' or x == 's':
                        print ( "\nOPCAO INVALIDA!\n" )
                        break

        elif pergunta == '2': # opcao de listar por letra/nome
            askLetter = input ( "\nListar todos os 'Generos' pela LETRA/NOME:" )
            db.cursor.execute ( "Select * FROM genres WHERE Name like'" + askLetter + "%'" )
            self.results = db.cursor.fetchall()
            view.apresentacao_dados_generos() # view para ver como os dados do genero sao apresentados

            for i, row in enumerate( self.results, start=1 ): # vai numerar os resultados do genero a começar do 1
                print ( row )

                if i % 10 == 0: # if para apenas mostrar 10 generos de cada vez e enter para listar mais
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

    def inserir_genres(self): # Funcao para inserir novos generos
        db.__init__()
        print ( "\nEsta prestes a INSERIR dados na tabela 'Generos'." )
        self.name = input ( "Nome do genero: " )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM genres WHERE Name=?''', ( self.name, ) )
                exists = db.cursor.fetchall()

                if not exists: # se o genero nao existir ja na bd executa
                    db.cursor.execute ( '''INSERT INTO genres(Name)VALUES(?)''', ( self.name, ) )
                    db.getcommit()
                    print ( "\nDados inseridos com sucesso na tabela 'Generos' da base de dados." )
                    print ( "Genero:", self.name )

                else: # se o novo nome ja existe da erro
                    print ( "\nERRO! O Genero", self.name, "ja existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel inserir Artista! ")

        finally:
            db.closedb()

    def apagar_genres(self): # Funcao para apagar generos
        db.__init__()
        print ( "\nEsta prestes a APAGAR dados da tabela 'Generos'." )
        self.name = input ( "Nome do Genero:" )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM genres WHERE Name=?''', ( self.name, ) )
                exists = db.cursor.fetchall()

                if exists: # se o nome do genero existir na bd continua e apaga
                    db.cursor.execute('''DELETE FROM genres WHERE Name = ? ''', ( self.name, ) )
                    db.getcommit()
                    print ( "\nO Genero,",self.name,"foi eliminado com sucesso!" )

                else: # senao da erro
                    print ( "\nERRO! O Genero", self.name, "nao existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel APAGAR o Genero!" )

        finally:
            db.closedb()

    def alterar_genres(self): # Funcao para alterar os dados de cada genero
        db.__init__()
        print ( "\nEsta prestes a ALTERAR dados da tabela 'Generos'." )
        self.name = input ( "\nInsira o NOME do Genero que pretende Alterar: " )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM genres WHERE Name = ? ''', ( self.name, ) )
                exists1 = db.cursor.fetchall()

                if exists1: # se existir o nome do genero pode colocar o novo nome
                    new_genre = input ( "Insira o novo NOME do Genero: " )
                    db.cursor.execute ( '''SELECT Name FROM genres WHERE Name = ? ''', ( new_genre, ) )
                    exists = db.cursor.fetchall()

                    if not exists: # se nao existir o novo nome na bd e alterado
                        db.cursor.execute ( '''UPDATE genres SET Name = ? WHERE Name = ? ''', ( new_genre, self.name ) )
                        db.getcommit()
                        print ( "\nO Nome do Genero foi alterado com sucesso!")
                        print ( "O Genero", self.name, "possui um novo Nome:", new_genre )

                    else: # se o novo nome ja existe da erro
                        print ( "\nERRO! O Genero", new_genre, "ja existe!" )

                else: # se o genero nao existir na bd
                    print ( "\nERRO! O Genero",self.name,"nao existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel ALTERAR o Genero!" )

        finally:
            db.closedb()


