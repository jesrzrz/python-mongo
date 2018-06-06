'''
Created on 6 jun. 2018

@author: jrodriguez
'''
import datetime
import json
from flask import Flask
from flask import request
from jr.gsearch import GoogleSearchModule
from jr.repository import GoogleSearchResultsRepository


app = Flask(__name__)

@app.route("/search")


def search():
    q = request.args.get('q', default = 1, type = str)    
    res = GoogleSearchModule.gSearchModule(q) 
     
    #transform data
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
        tempResult['date'] : datetime.datetime.utcnow()
        #print(item['pagemap']['metatags'])
        result.append(tempResult)        
        json_data = json.dumps(result)
     

    GoogleSearchResultsRepository.GoogleSearchResultRepository.insertResults(json_data) 
       
    return q


if __name__ == '__main__':
    app.run(debug=True)