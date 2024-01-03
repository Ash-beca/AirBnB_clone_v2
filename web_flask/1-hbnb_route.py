#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """sends a GET request to the homepage"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """sends a GET request to the hbnb page"""
    return ("HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    