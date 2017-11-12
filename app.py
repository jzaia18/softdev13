from flask import Flask, render_template
import urllib2
import random
from json import loads

app = Flask(__name__)
api_url = "http://pokeapi.co/api/v2/pokemon"

def get_bulk_data(num):
    url = api_url + '/' + num
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    json = opener.open(url)
    json = json.read()
    return loads(json)
    
def get_flavor_text(num):
    url = api_url + '-species/' + num
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    json = opener.open(url)
    json = json.read()
    
    # get English description
    for each in loads(json)["flavor_text_entries"]:
        if each['language']['name']=='en':
            return each['flavor_text']
    return ''

@app.route('/')
def root():
    num = str(int(random.random() * 802 + 1))
    data = get_bulk_data(num)
    flavor = get_flavor_text(num)
    return render_template('index.html', data = data, num = num, flavor = flavor)

if __name__ == '__main__':
    app.debug = True
    app.run()
