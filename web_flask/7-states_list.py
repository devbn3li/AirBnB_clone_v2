#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Display text"""
    return 'Hello HBNB!'
@app.route('/hbnb')
def hbnb():
    """Display text"""
    return 'HBNB'
@app.route('/c/<text>')
def c(text):
    """Display text"""
    return 'C %s' % text.replace('_', ' ')
@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """Display text"""
    return 'Python %s' % text.replace('_', ' ')
@app.route('/number/<int:n>')
def number(n):
    """Display text"""
    return '%d is a number' % n
@app.route('/number_template/<int:n>')
def number_template(n):
    """Display text"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Display text"""
    return render_template('6-number_odd_or_even.html', n=n)

@app.route('/states_list')
def states_list():
    """Display text"""
    return render_template('7-states_list.html')

@app.teardown_appcontext
def teardown_db(exception):
    """Close storage"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
