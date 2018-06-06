'''
Created on 6 jun. 2018

@author: jrodriguez
'''
import codecs
import json
import pprint
import sys

from googleapiclient.discovery import build
import pkg_resources


'config'

resource_package = 'config.json'  
resource_path = '/'.join(('config'))  
template = pkg_resources.resource_string(resource_package, resource_path)

with open(template, 'r') as f:
    config = json.load(f)
    
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
