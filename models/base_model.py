#!/usr/bin/env python3
""" this is the module for the base class """
from datetime import datetime
import uuid
import json

filename = 'storage.json'


class BaseModel:
    """this is the class BaseModel for our AirBNB clone which other classes will inherite from """

    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel instance. """

        if kwargs is not None and kwargs != {}:
	""" here we assign values to the various keys passed or not passed with the class """
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%d/%m/%y %H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%d/%m/%y %H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            # TODO: add storage

    def __str__(self):
        """ returns a string format of the class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
    """ returns a dictionary representation of the class"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

    def save(self):
    """ changes the time of the updated_at attr to the current time """
        self.updated_at = datetime.now
