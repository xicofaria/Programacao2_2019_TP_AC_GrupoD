import sqlite3


class db(object):
    def __init__(self):
        self.connection = sqlite3.connect( "./chinook.db" )
        self.cursor = self.connection.cursor()

    def connection(self):
        self.connection = sqlite3.connect( "./chinook.db" )

    def getcursor(self):
        return self.cursor

    def getcommit(self):
        return self.connection.commit()

    def closedb(self):
        return self.connection.close()


