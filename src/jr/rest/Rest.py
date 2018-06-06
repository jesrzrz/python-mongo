'''
Created on 6 jun. 2018

@author: jrodriguez
'''
from flask import Flask
from flask import request
from jr.gsearch import GoogleSearchModule


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/search")
def search():
    q = request.args.get('q', default = 1, type = str)    
    GoogleSearchModule.gSearchModule(q)    
    return q


if __name__ == '__main__':
    app.run(debug=True)