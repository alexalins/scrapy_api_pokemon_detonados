from pokemonDetonados.app import app
from flask import jsonify
import json

@app.route('/')
def getDetonados():
    detonados = getJSON('app/../detonados.json')
    return jsonify(detonados)

@app.route('/spinoff')
def getSpinOff():
    spinoff = getJSON('app/../spinOff.json')
    return jsonify(spinoff)

def getJSON(path):
   with open(path, 'r') as f:
    return json.load(f)
 