#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """

    def __init__(self):
        """Initializes"""
        self.__file_path = str(file.json)
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""

    return __objects.__dict__

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj = json.dumps(self, default=self.__objects)
        return obj

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            self.__object = json.load(self.__file_path)
        except:
            pass
