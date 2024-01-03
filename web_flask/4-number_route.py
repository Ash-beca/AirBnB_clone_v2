#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """sends a GET request to the homepage"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """sends a GET request to the hbnb page"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """sends a GET request to the c page"""
    return ('C %s' % escape(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python',
           defaults={'text': 'is cool'}, strict_slashes=False)
def display_python(text):
    """sends a GET request to the python page"""
    return ('Python %s' % escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """sends a GET request to the number page"""
    return ('%d is a number' % n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')