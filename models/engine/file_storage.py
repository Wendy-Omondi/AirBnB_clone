#!/usr/bin/python3
class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""


    def __init__(self):
        """Initializes"""
        self.__file_path = str(file.json)
        self.__objects = pass

    def all(self):
        """returns the dictionary __objects"""
        return __objects.__dict__

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        
