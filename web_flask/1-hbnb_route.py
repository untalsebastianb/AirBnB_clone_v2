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

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
