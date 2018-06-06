'''
Created on 6 jun. 2018

@author: jrodriguez
'''
import json
import os
from googleapiclient.discovery import build

#config file
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../../config/config.json")

#read config file
with open(path) as json_data:
    config = json.load(json_data)
    
#read properties
gsearch_apikey = config['DEFAULT']['GOOGLE_SEARCH_API_KEY'] 
gsearch_cx = config['DEFAULT']['GOOGLE_SEARCH_CX']

#module definition
def gSearchModule(searchTerm):    
# Build a service object for interacting with the API. Visit
# the Google APIs Console <http://code.google.com/apis/console>
# to get an API key for your own application.
    gSearchService = build("customsearch", "v1", developerKey=gsearch_apikey)
# call to g api
    res = gSearchService.cse().list(q=searchTerm, cx=gsearch_cx).execute()  
    return res