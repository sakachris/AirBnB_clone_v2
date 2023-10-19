#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    /hbnb: display “HBNB”
    """
    return "HBNB"


if __name__ == "__main__":
    """listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
