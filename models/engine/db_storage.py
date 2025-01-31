#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''
        Create SQLalchemy database
    '''
    __engine = None
    __session = None
    classes = {"User": User, "BaseModel": BaseModel,
               "Place": Place, "State": State,
               "City": City, "Amenity": Amenity,
               "Review": Review}

    def __init__(self):
        '''
            Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)
        '''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns dictionary with all objects depending
        of the class name (argument cls)"""
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        else:
            for key, value in DBStorage.classes.items():
                if key != "BaseModel":
                    objs = self.__session.query(value).all()

        db_dict = {}
        for obj in objs:
            # k = f"{type(obj).__name__}.{obj.id}"
            k = f"{obj.__class__.__name__}.{obj.id}"
            db_dict[k] = obj
        return db_dict

    def new(self, obj):
        """Add the object to the current
        database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current
        database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
            Commit all changes of current database session
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''
            Removes the session.
        '''
        self.__session.close()
