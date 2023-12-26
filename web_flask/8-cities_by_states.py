#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the main HBNB page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    reviews = storage.all(Review).values()
    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           places=places, users=users, reviews=reviews)


@app.teardown_appcontext
def teardown(self):
    """Method to remove SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
