#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ['HBNB_ENV'] == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            from models import storage
            var = storage.all('City')
            list_cities = []
            for key, value in var.items():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
