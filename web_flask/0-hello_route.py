#!/usr/bin/python3
"""
Creating a server with flask
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def sayHello():
    """Function to say hello"""
    return 'Hello HBNB!'
