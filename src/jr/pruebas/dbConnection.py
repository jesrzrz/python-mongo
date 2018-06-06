'''
Created on 6 jun. 2018

@author: jrodriguez
'''
from pymongo import MongoClient
import json
import os
import datetime

'main'
def main():
    
    # config file
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../../config/config.json")

# read config file
    with open(path) as json_data:
        config = json.load(json_data)
    
# read properties
    mongoDs = config['DEFAULT']['MONGO_DS'] 

    client = MongoClient(mongoDs)

# data base name : 'test-database-1'
    mydb = client['test-database-1']

    

    myrecord = {
        "author": "Duke",
        "title" : "PyMongo 101",
        "tags" : ["MongoDB", "PyMongo", "Tutorial"],
        "date" : datetime.datetime.utcnow()
        }

    record_id = mydb.mytable.insert(myrecord)

    print (record_id)
    print (mydb.collection_names())

if __name__ == '__main__':
    main()
    
