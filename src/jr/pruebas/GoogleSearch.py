'''
Created on 6 jun. 2018

@author: jrodriguez
'''
import pprint
import json
import sys
import codecs

from googleapiclient.discovery import build

'config'

with open('config.json', 'r') as f:
    config = json.load(f)
    
gsearch_apikey = config['DEFAULT']['GOOGLE_SEARCH_API_KEY'] 
gsearch_cx = config['DEFAULT']['GOOGLE_SEARCH_CX']


'main'
def main():
    
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  gSearchService = build("customsearch", "v1", developerKey = gsearch_apikey)

  #call to g api
  res = gSearchService.cse().list( q = 'ion kpact', cx = gsearch_cx).execute()
  
  #JSON object
  jsonParent = json.loads(json.dumps(res))
  jsonItems = jsonParent['items'] 
  
  
  #iterate through JSON
  for item in jsonItems:
    print(item['title'])
    print(item['link'])
    print(item['htmlSnippet'])
    
  
  #pprint.pprint(res)

if __name__ == '__main__':
    main()