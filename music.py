# importes dos ficheiros views e db
import sqlite3
from db import db
from view import views

# instancias
db = db()
view = views()


class musics: # classe para as musicas

    def __init__(self, TrackId=None, Name=None, AlbumId=None, MediaTypeId=None, GenreId=None, Composer=None, Miliseconds=None, Bytes=None, UnitPrice=None):
        self.TrackId =       TrackId
        self.Name =          Name
        self.AlbumId =       AlbumId
        self.MediaTypeId =   MediaTypeId
        self.GenreId =       GenreId
        self.Composer =      Composer
        self.Milliseconds =  Miliseconds
        self.Bytes =         Bytes
        self.UnitPrice =     UnitPrice

    def show_musics(self): # Funcao para listar as musicas
        db.__init__()
        pergunta = input ( "\n1.Listar TODAS as Musicas | 2.Listar POR LETRA/NOME as Musicas:" )
        # Uma pergunta feita para saber se pretende listar tudo ou por nome/letra

        if pergunta == '1': # se escolher todas as musicas
            db.cursor.execute ( "select TrackId, Name, AlbumId, GenreId, Composer, Milliseconds, Bytes, UnitPrice from tracks limit 00,5000;" )
            self.results = db.cursor.fetchall()
            view.apresentacao_dados_musicas() # view para ver como os dados da musica sao apresentados

            for i, row in enumerate( self.results, start=1 ): # vai numerar os resultados da musica a começar do 1
                print ( row )

                if i % 20 == 0: # if para apenas mostrar 20 musicas de cada vez e enter para listar mais
                    x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!:" )

                    if x == '':
                        continue

                    elif x == 'S' or x == 's':
                        break

                    elif x != 'S' or x == 's':
                        print ( "\nOPCAO INVALIDA!\n" )
                        break

        elif pergunta == '2': # opcao de listar por letra/nome
            askLetter = input ( "\nListar TODAS as 'Musicas' pela LETRA/NOME:" )
            db.cursor.execute ( "Select Name FROM tracks WHERE Name like'" + askLetter + "%'" )
            exists1 = db.cursor.fetchall() # serve para verificar se existe a musica na bd

            if exists1: # se o nome da musica existir na bd continua
                db.cursor.execute ( "Select  TrackId, Name, AlbumId, GenreId, Composer, Milliseconds, Bytes, UnitPrice FROM tracks WHERE Name like'" + askLetter + "%'" )
                self.results = db.cursor.fetchall()
                view.apresentacao_dados_musicas() # view para ver como os dados da musica sao apresentados

                for i, row in enumerate( self.results, start=1 ): # vai numerar os resultados da musica a começar do 1
                    print( row )

                    if i % 10 == 0: # if para apenas mostrar 10 musicas de cada vez e enter para listar mais
                        x = input ( "\nPressione 'ENTER' para listar mais ou 'S' para sair!:" )

                        if x == '':
                            continue

                        elif x == 'S' or x == 's':
                            break

                        elif x != 'S' or x == 's':
                            print ( "\nOPCAO INVALIDA!\n" )
                            break

            else: # se a musica nao existir
                print ( "\nERRO! A Musica", askLetter, "nao existe!" )

        else: # uma opcao diferente das disponiveis
            print ( "\nESCOLHA UMA OPCAO VALIDA!\n" )

    def inserir_musics(self): # Funcao para inserir novas musicas
        db.__init__()
        print ( "\nEsta prestes a INSERIR dados na tabela 'Musicas'." )

        while True: # ciclo while para pedir informacoes da musica ao utilizador
            try:
                self.Name =         input ( "\nNome da Musica: ")
                self.AlbumId =      int ( input( "ID do Album: ") )
                self.MediaTypeId =  int ( input( "ID MediaType: ") )
                self.GenreId =      int ( input( "ID do Genero: ") )
                self.Composer =     input ( str( "Compositor: ") )
                self.Milliseconds = int ( input( "Milisegundos: ") )
                self.Bytes =        int ( input( "Bytes: ") )
                self.UnitPrice =    float ( input( "Preco Unidade: ") )

                if self.Name == '' or self.Name == ' ': # nome vazio da erro
                    print ( "\nERRO! INSIRA O NOME DA MUSICA!" )
                    break

                elif self.MediaTypeId == '' or self.MediaTypeId == ' ': # mediatype vazio da erro
                    print ( "\nERRO! INSIRA O MEDIA TYPE DA MUSICA!" )
                    break

                elif self.Milliseconds == '' or self.Milliseconds == ' ': # milisegundos vazio da erro
                    print ( "\nERRO! INSIRA O TEMPO MILISEGUNDOS DA MUSICA!" )
                    break

                elif self.UnitPrice == '' or self.UnitPrice == ' ': # preco unitario vazio da erro
                    print ( "\nERRO! INSIRA O PRECO UNITARIO DA MUSICA!" )
                    break

            except ValueError as error: # qualquer outro erro que possa acontecer
                print ( "\nErro de Parametro! Valor Inteiro/Decimal/Vazio!" )
                print ( "Erro:", error )
                break

            else: # continua senao houver erros nenhums
                try:
                    with db.connection:
                        db.__init__()
                        db.cursor.execute('''INSERT INTO tracks(Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice) VALUES(?,?,?,?,?,?,?,?)''',
                                     (self.Name, self.AlbumId, self.MediaTypeId, self.GenreId, self.Composer, self.Milliseconds, self.Bytes, self.UnitPrice))
                        db.getcommit()

                        print ( "\nDados inseridos com sucesso na tabela 'Musicas' da base de dados.")
                        print ( "\nNome:",       self.Name)
                        print ( "ID do Album:",  self.AlbumId)
                        print ( "ID MediaType:", self.MediaTypeId)
                        print ( "ID Genero:",    self.GenreId)
                        print ( "Compositor:",   self.Composer)
                        print ( "Milisegundos:", self.Milliseconds)
                        print ( "Bytes:",        self.Bytes)
                        print ( "Preco Unidade:",self.UnitPrice)

                except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
                    print ( "\nERRO! Impossivel inserir Musica!" )
                    print ( sqlite3.IntegrityError())

                finally:
                    db.closedb() # fecha a bd

    def apagar_musics(self): # Funcao para apagar musicas
        db.__init__()
        print ( "\nEsta prestes a APAGAR dados da tabela 'Musicas'." )
        self.Name = input ( "Nome da Musica: " )

        try:
            with db.connection:
                db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name=?''', ( self.Name, ))
                exists = db.cursor.fetchall()

                if exists: # se o nome da musica existir na bd continua e apaga
                    db.cursor.execute( '''DELETE FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    db.getcommit()
                    print ( "\nA Musica",self.Name,"foi eliminada com sucesso!" )

                else: # senao da erro
                    print ( "\nERRO! A Musica",self.Name,"nao existe!" )

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel APAGAR a Musica!" )

        finally:
            db.closedb()

    def alterar_musics(self): # Funcao para modificar os dados de cada musica
        db.__init__()
        print ( "\nEsta prestes a ALTERAR dados da tabela 'Musicas'" )
        view.escolha_operacao() # view para ver as escolhas de operacao
        alt1 = input ( "\nEscolha Opcao: ")

        try:
            with db.connection:
                if alt1 == '1': # a escolha um para alterar o nome da musica
                    self.Name = input (" \nInsira o Nome da Musica que pretende alterar: " )
                    db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    exists1 = db.cursor.fetchall()

                    if exists1: # se existir o nome da musica pode colocar o novo nome
                        new_name = input ( "Insira o NOVO Nome da Musica: " )

                        if new_name != '': # nome introduzido altera o nome
                            db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( new_name, ))
                            exists = db.cursor.fetchall()

                        else: # nome vazio da erro
                            print ( "ERRO! Tem de inserir um NOME!" )
                            return

                        if not exists: # se nao existir o novo nome na bd e alterado
                            db.cursor.execute ( '''UPDATE tracks SET Name = ? WHERE Name = ? ''', ( new_name, self.Name ))
                            db.getcommit()
                            print ( "\nO Nome da Musica foi alterado com sucesso!" )
                            print ( "A Musica",self.Name,"possui um novo Nome:", new_name)

                        else: # se o novo nome ja existe da erro
                            print ( "\nERRO! A Musica",new_name,"ja existe!")

                    else: # se a musica nao existir na bd
                        print ( "\nERRO! A Musica",self.Name,"nao existe!")

                elif alt1 == '2': # se escolher a operacao de mudar id do artista
                    self.Name = input ( "\nInsira o Nome da Musica que pretende alterar o ID do Album: ")
                    db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    exists = db.cursor.fetchall() # guarda o nome da musica para ver se existe na bd

                    if exists: # se existir pode continuar
                        new_albumid = input ( "Insira o NOVO ID do Album: ")
                        db.cursor.execute ( '''UPDATE tracks SET ArtistId = ? WHERE Name = ? ''', ( new_albumid, self.Name ))
                        db.getcommit()
                        print ( "\nID do Album alterado com sucesso!")
                        print ( "A Musica",self.Name,"possui um novo Album com o ID:", new_albumid)

                    else: # senao existir da erro
                        print ( "\nERRO! A Musica nao existe!")

                elif alt1 == '3': # se escolher a operacao de mudar id do genero
                    self.Name = input ( "\nInsira o Nome da Musica que pretende alterar o ID do Genero: ")
                    db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    exists = db.cursor.fetchall() # guardar o nome da musica para ver se existe na bd

                    if exists: # se existir pode continuar
                        new_genreid = input ( "Insira o NOVO ID do Genero: ")
                        db.cursor.execute ( '''UPDATE tracks SET GenreId = ? WHERE Name = ? ''',(new_genreid, self.Name))
                        db.getcommit()
                        print ( "\nID do Genero alterado com sucesso!")
                        print ( "A Musica", self.Name, "possui um novo Genero com o ID:", new_genreid )

                    else: # senao existir da erro
                        print ( "\nERRO! A Musica nao existe!")

                elif alt1 == '4': # se escolher a operacao de mudar o compositor
                    self.Name = input ( "\nInsira o Nome da Musica que pretende alterar o Compositor: ")
                    db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    exists = db.cursor.fetchall()

                    if exists: # se existir pode continuar
                        new_composer = input ( "Insira o NOVO Compositor: ")
                        db.cursor.execute ( '''UPDATE tracks SET Composer = ? WHERE Name = ? ''',( new_composer, self.Name ))
                        db.getcommit()
                        print ( "\nCompositor alterado com sucesso!")
                        print (" A Musica", self.Name, "possui um novo Compositor:", new_composer )

                    else: # senao existir da erro
                        print ( "\nERRO! A Musica nao existe!")

                elif alt1 == '5': # se escolher a operacao de mudar os milisegundos
                    self.Name = input ( "\nInsira o Nome da Musica que pretende alterar os MiliSegundos: ")
                    db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    exists = db.cursor.fetchall()

                    if exists: # se existir pode continuar
                        new_milliseconds = input (" Insira o NOVO Tempo MiliSegundos: ")
                        db.cursor.execute ( '''UPDATE tracks SET Milliseconds = ? WHERE Name = ? ''',( new_milliseconds, self.Name ))
                        db.getcommit()
                        print ( "\nMiliSegundos alterado com sucesso!")
                        print ( "A Musica", self.Name, "possui um novo Tempo MiliSegundos:", new_milliseconds )

                    else: # senao existir da erro
                        print ( "\nERRO! A Musica nao existe!")

                elif alt1 == '6': # se escolher a operacao de mudar os bytes
                    self.Name = input ("\nInsira o Nome da Musica que pretende alterar os Bytes: ")
                    db.cursor.execute('''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                    exists = db.cursor.fetchall()

                    if exists: # se existir pode continuar
                        new_bytes = input ( "Insira o NOVO Tamanho Bytes: ")
                        db.cursor.execute ( '''UPDATE tracks SET Bytes = ? WHERE Name = ? ''',( new_bytes, self.Name ))
                        db.getcommit()
                        print ( "\nBytes alterado com sucesso!")
                        print (" A Musica", self.Name, "possui um novo Tamanho Bytes:", new_bytes )

                    else: # senao existir da erro
                        print ( "\nERRO! A Musica nao existe!")

                elif alt1 == '7':  # se escolher a operacao de mudar o preco unitario
                        self.Name = input ( "\nInsira o Nome da Musica que pretende alterar o Preco Unitario: ")
                        db.cursor.execute ( '''SELECT Name FROM tracks WHERE Name = ? ''', ( self.Name, ))
                        exists = db.cursor.fetchall()

                        if exists: # se existir pode continuar
                            new_unitprice = input ( "Insira o NOVO Preco Unitario: ")
                            db.cursor.execute ( '''UPDATE tracks SET UnitPrice = ? WHERE Name = ? ''',( new_unitprice, self.Name ))
                            db.getcommit()
                            print ( "\nPreco Unitario alterado com sucesso!")
                            print ("A Musica", self.Name, "possui um novo Preco Unitario:", new_unitprice )

                        else: # senao existir da erro
                            print ( "\nERRO! A Musica nao existe!")

                else: # caso escolha uma outro opcao da erro
                    print ( "\nEscolha uma opcao valida!")

        except sqlite3.IntegrityError: # qualquer outro erro que possa acontecer
            print ( "\nERRO! Impossivel ALTERAR a Musica!")

        finally:
            db.closedb()


