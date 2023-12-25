#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """/hbnb route : display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def dynamic_route(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def dynamic_route_pyton(text="is cool"):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display HTML only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display Number: n is even|odd in HTML only if n is an integer."""

    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
