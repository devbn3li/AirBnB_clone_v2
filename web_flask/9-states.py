#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """A function that serves as the home route of the application.
    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a html page with states and cities"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_context(self):
    """Closes the storage session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
