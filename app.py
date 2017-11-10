from flask import Flask, render_template
import urllib2 as u
from json import loads

app = Flask(__name__)
api_url = "https://api.nasa.gov/planetary/apod?api_key=tbTCi4JbCHJ7zrVjTb9Na7ksIJPkTxPoymdAoBJi"

@app.route('/')
def root():
    json = u.urlopen(api_url).read()
    data = loads(json)
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.debug = True
    app.run()
