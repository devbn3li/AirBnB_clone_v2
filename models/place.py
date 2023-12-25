#!/usr/bin/python3
"""Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship(
        "Amenity", secondary=place_amenity, viewonly=False)
    if os.environ['HBNB_ENV'] != 'db':
        @property
        def reviews(self):
            """Getter method to retrieve related Review instances."""
            from models import storage
            dic = storage.all('Review')
            return [].append(v for k,
                             v in dic.items() if self.id == v['place_id'])

        @property
        def amenities(self):
            """Getter method to retrieve related Amenity instances."""
            from models import storage
            dic = storage.all('Amenity')
            return [].append(v for k,
                             v in dic.items() if self.id == v['amenity_ids'])

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
