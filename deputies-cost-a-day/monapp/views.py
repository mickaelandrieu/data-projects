from flask import Flask, url_for

import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    return '<img src="'+ url_for('static', filename='img/camembert.png')+'" />'
