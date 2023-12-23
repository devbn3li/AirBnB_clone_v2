#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Return Python followed by text"""

    return 'Python %s' % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return n is a number if n is an integer"""

    return '%d is a number' % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return HTML page if n is an integer"""

    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
