from db import db
import sqlite3
import hashlib
import getpass
import sys

db = db()


class encryptar:
    # class para cryptografar password em md5
    def criarPass(self):
        if sys.stdin.isatty():  # Quando é executado no terminal ira ser executado o comandos para "esconder a password"
            print ( '\nInsira uma password:' )
            pswd = getpass.getpass('')

        else:
            # Password no Idle
            print ( 'Insira uma password:' )
            pswd = sys.stdin.readline().strip()
        password = hashlib.md5()  # Vai criptografar a password em hash MD5
        password.update ( pswd.encode ( "utf-8" ) )  # Conversão da password para utf-8
        return password.hexdigest()


en = encryptar()


class contas(object):  # Criaçao da class contas.

    def __init__(self, id=None, nome=None, password=None, resp=None, resp2=None, resp3=None):
        self.id = id
        self.nome = nome
        self.password = password
        self.resp = resp
        self.resp = resp2
        self.resp = resp3

    def inserirContas(self):  # Função para criar tabela utilizadores caso não exista, com os seus devidos atributos.
        db.cursor.executescript(
            "CREATE TABLE IF NOT EXISTS utilizadores (id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar(64),"
            "password varchar(150) )" )
        db.getcommit()

    def verificarContas(self):  # Função para verificar se a tabela utilizadores esta vazia, caso esteja vai criar o utilizador admin com a password admin
        db.cursor.execute ( "SELECT * FROM utilizadores" )
        db.getcommit()
        admin = db.cursor.fetchall()

        if len ( admin ) == 0:
            db.cursor.execute ( "INSERT INTO utilizadores Values('1','admin','21232f297a57a5a743894a0e4a801fc3')" )
            db.cursor.execute ( "SELECT * FROM utilizadores" )
            db.getcommit()
            results = db.cursor.fetchall()  # Verificar os resultados obtidos

            for row in results:
                print(row)
        db.closedb()

    def newUser(self):  # Função para fazer o registo de um novo utilizador à base de dados.
        db.__init__()
        self.nome = input ( ( 'Username:' ) )
        db.cursor.execute ( 'SELECT nome FROM utilizadores WHERE nome = ?', ( self.nome, ) )
        verifica_nome = db.cursor.fetchall()

        if len ( verifica_nome ) > 0:
            print ( 'Ja existe pessoas com esse nome!\nTente outro' )

        else:
            self.password = en.criarPass()
            db.__init__()
            db.cursor.execute ( '''INSERT INTO utilizadores (id, nome, password)
                      VALUES(?,?,?)''', ( self.id, self.nome, self.password ) )
            db.getcommit()
            print ( "\nRegisto completado com sucesso!\n" )
            import main

    def oldUser(self):  # Função para verificar a existecia de um utilizador na base de dados e fazer o seu respetivo login
        db.__init__()
        self.nome = input ( "\nInsira o seu username:" )
        self.password = en.criarPass()
        hashlib.md5 ( self.password.encode ( 'utf8' ) ).hexdigest()  # conveter a password string para md5
        # Fazer pesquisa na base de dados, com o nome e a respetiva password
        db.cursor.execute ( "SELECT * FROM utilizadores WHERE nome= ? and password= ?",
                          ( self.nome, self.password ) )
        found = db.cursor.fetchone()

        if self.nome == "admin" and self.password == "21232f297a57a5a743894a0e4a801fc3":  # Caso o nome e a password forem admin entra no menu admin
            import admin

        elif found:
            print ( "\nLogin feito com sucesso!\n" )
            import main

        else:
            print ( "\nUsername ou a password não existem\n" )

    def menuUser(self):  # Função para a criação de um menu para serem realizadas as operações.

        while self.resp != 3:
            print ( """\nBEM-VINDO:
 
             1. Login 
             2. Registar 
             3. Sair do programa""" )

            self.resp = input ( '\nEscolha uma opção: ' )

            if self.resp == "1":
                self.oldUser()

            elif self.resp == "2":
                self.newUser()

            elif self.resp == "3":
                print ( "\nA Sair do Programa! Obrigado! Ate-breve!" )
                sys.exit()


exec = contas()
exec.inserirContas()
exec.verificarContas()
exec.menuUser()
