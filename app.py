# -- Initialization section --
# ---- YOUR APP STARTS HERE ----
# -- Import section --

from flask import Flask
from flask import render_template
from flask import request
from flask import session
import requests #To access our API

# -- Initialization section --
app = Flask(__name__)
## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'
# -- Routes section --

@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Angel"
    return render_template('index.html')
    
@app.route("/random")
def jeopardy_random():
    #Used jservice api/random to get one jeopardy clue
    response = requests.get('http://jservice.io/api/random?count=1').json()
    category = response[0]["category"]["title"]
    value = response[0]["value"]
    question = response[0]["question"]
    return render_template("random_clue.html", category= category, value=value, question=question)