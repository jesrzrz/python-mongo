'''
Created on 7 jun. 2018

@author: Heret_2
'''
from jr.dbConnection import DatabaseConnectionModule

class GoogleSearchResultRepository():
    def __init__(self):
        self.db = 'app'
        self.tabla = 'gSearchResults'
        self.connection = DatabaseConnectionModule.DbConnection(self.db, self.tabla)
        
    def insertResults(self, objetos):
        self.connection.dbConnectionInsertMany(objetos)
        
    def insertResult(self, objeto):
        self.connection.dbConnectionInsert(objeto)