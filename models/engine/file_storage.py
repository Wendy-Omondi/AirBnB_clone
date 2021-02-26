#!usr/bin/python3
"""Defines the file storage class."""


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serializes an instance to JSON and

    deserializes back to instance object

    """
    __objects = {}

    __file_path = "file.json"

    def all(self, cls=None):

        """Returns a dictionary of __objects"""

        return self.__objects

    def new(self, obj):

        """Sets in __ojbects the obj with key <obj class name >.id"""

        if obj is not None:

            # Concatenate class object name with id.

            key = obj.__class__.__name__+"."+obj.id

            # update the object dict with the new key and object as value.

            self.__objects[key] = obj

    def save(self):

        """" Serializes __objects to the JSON File(path:__file_path)"""

        j_obj = {}
        # convert to a dictionary for json to understand using
        # to_dict method of the basemodel class
        # The result of this will be a key with a unique dict as the value.

        for key in self.__objects:

            j_obj[key] = self.__objects[key].to_dict()

        # Convert the dictionary into json and save in __filepath.

        with open(self.__file_path, 'w') as f:

            json.dump(j_obj, f)

    def reload(self):

        """

        Deserializes the JSON file to objects

        exists; otherwise does nothing, no exception should be raised

        if the file does not exist.

        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except:

            pass
