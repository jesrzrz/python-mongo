'''
Created on 6 jun. 2018

@author: Heret_2
'''
from pymongo import MongoClient
import json
import os
    
class DbConnection():   
    
    def __init__(self, bd, tabla):
        self.bd = bd
        self.tabla = tabla
    
        # config file
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../config/config.json")
    
        # read config file
        with open(path) as json_data:
            config = json.load(json_data)
        
        # read properties
        self.mongoDs = config['DEFAULT']['MONGO_DS'] 
    
    def dbConnectionInsertMany(self, objetos):    
        client = MongoClient(self.mongoDs)    
        # data base name : 'test-database-1'
        mydb = client[self.bd]
        record_id = mydb.getattr(self.tabla).insert_many(objetos)
        print(record_id)
        
    def dbConnectionInsert(self, objeto):
        client = MongoClient(self.mongoDs)    
        # data base name : 'test-database-1'
        mydb = client[self.bd]
        record_id = mydb.getattr(self.tabla).insert_many(objeto)
        print(record_id)
