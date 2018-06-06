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
  
# JSON object
    jsonParent = json.loads(json.dumps(res))
    jsonItems = jsonParent['items'] 
  
# iterate through JSON
    result = []

    for item in jsonItems:
        tempResult = {}        
        tempResult['title'] = item['title']
        tempResult['link'] = item['link']
        tempResult['htmlSnippet'] = item['htmlSnippet'] 
        #print(item['title'])
        #print(item['link'])
        #print(item['htmlSnippet'])        
        if 'pagemap' not in item:
            continue
        if 'metatags' not in item['pagemap']:
            continue
        tempResult['metatags'] = item['pagemap']['metatags']
        #print(item['pagemap']['metatags'])
        result.append(tempResult)
        
    json_data = json.dumps(result)
