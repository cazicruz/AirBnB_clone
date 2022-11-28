#!/usr/bin/env python3
from datetime import datetime
import uuid
import json
from models import storage


class BaseModel:
    """this is the Base Model for our AirBNB clone """

    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel instance. """

        if kwargs is not None and kwargs != {}:
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
            storage.new(self)
            # TODO: add storage

    def __str__(self):
        """ returns a string format of the class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        def save(self):
        self.updated_at = datetime.now
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
