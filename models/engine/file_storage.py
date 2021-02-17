#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """

    def __init__(self):
        """Initializes"""
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        o_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        o_d = FileStorage.__objects
        o_dic = {obj: o_d[obj].to_dict() for obj in o_d.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(o_dic, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                o_dic = json.load(f)
                for o in o_dic.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
