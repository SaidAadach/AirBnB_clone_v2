#!/usr/bin/python3
"""Démarre une application web Flask"""
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """Retourne une chaîne de caractères à la route /airbnb-onepage/"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
