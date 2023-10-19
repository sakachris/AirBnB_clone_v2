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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    display c followed by <text>
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    """listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
