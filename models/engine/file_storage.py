#!/usr/bin/env python3
""" Module for FileStorage class"""
import json
import datetime
import os


class FileStorage:
    """ file storage class"""
    __file_path = "file.json"
    __objects = { }

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w") as f:
            json.dump('FileStorage.__objects', f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing.
         If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            return

