'''
Created on 6 jun. 2018

@author: jrodriguez
'''
import codecs
import json
import pprint
import sys
import os
import pkg_resources
from googleapiclient.discovery import build

'config'
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../../config/config.json")

with open(path) as json_data:
    config = json.load(json_data)
    
gsearch_apikey = config['DEFAULT']['GOOGLE_SEARCH_API_KEY'] 
gsearch_cx = config['DEFAULT']['GOOGLE_SEARCH_CX']


'main'
def gSearchModule( searchTerm ):
    
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  gSearchService = build("customsearch", "v1", developerKey = gsearch_apikey)

  #call to g api
  res = gSearchService.cse().list( q = searchTerm, cx = gsearch_cx).execute()
  
  #JSON object
  jsonParent = json.loads(json.dumps(res))
  jsonItems = jsonParent['items'] 
  
  
  #iterate through JSON
  for item in jsonItems:
    print(item['title'])
    print(item['link'])
    print(item['htmlSnippet'])
