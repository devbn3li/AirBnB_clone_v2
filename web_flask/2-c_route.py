#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return hello hbnb"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return hbnb"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return C followed by text"""

    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
