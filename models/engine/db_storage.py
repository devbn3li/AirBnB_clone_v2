#!/usr/bin/python3
"""DB Storage Engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """DB Storage Class"""

    __engine = None
    __session = None

    def __init__(self):
        """DBStorage Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database session"""
        if cls is None:
            query = self.__session.query(
                State, City, User, Place, Review, Amenity)
            result = query.all()
            return result
        else:
            query = self.__session.query(cls)
            result = query.all()
            return result

    def new(self, obj):
        """Add the object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close current session"""
        self.__session.close()
