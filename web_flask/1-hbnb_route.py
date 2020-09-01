#!/usr/bin/python3
"""
that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def sayHello():
    """Function to say hello"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def sayHello2():
    """Function to say hello"""
    return 'HBNB'
