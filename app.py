from flask import Flask, render_template
import urllib2
import random
from json import loads

app = Flask(__name__)
api_url = "http://pokeapi.co/api/v2/pokemon/"

@app.route('/')
def root():
    url = api_url + str(int(random.random() *802 + 1))
    print url
    req = urllib2.Request(url)
    #urllib2.Request.add_header('User-agent', 'Please work')
    json = urllib2.urlopen(url)
    json = json.read()
    data = loads(json)
    print "HOI!!!!"
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.debug = True
    app.run()
