#!usr/bin/python3
"""Defines the file storage class."""


import json
from models.base_model import BaseModel


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

        j_objects = {}

        # For the python data to be serialized the data stored inside the objec

        # variable as objects must be converted to a dictionary so that python

        # for json to understand using to_dict method of the basemodel class

        # The result of this will be a key with a unique dict as the value.

        for key in self.__objects:

            j_objects[key] = self.__objects[key].to_dict()

        # Convert the dictionary into json and save in __filepath.

        with open(self.__file_path, 'w') as f:

            json.dump(j_objects, f)

    def reload(self):

        """

        Deserializes the JSON file to objects

        exists; otherwise does nothing, no exception should be raised

        if the file does not exist.

        """

        try:

            with open(self.__file_path, 'r', encoding="utf8") as f:

                # The load method deserializes a json string into a python dict

                obj_dict = json.load(f)

            for obj_item in obj_dict.values():

                # Extract the class from which to instantiate an object.

                # Remember we loaded the values not the keys.

                class_name = obj_item["__class__"]

                # Since we are creating obj instances the attribute __class__

                # should not be supplied as part of the arguments to the init

                # function of the class(identified by class_name) all the other

                # arguments are valid.

                del obj_item["__class__"]

                # Use the previously defined new function to create a new obj.

                # The double asterics expands the dictionary to allow every key

                # value pair from obj_item dict to be passed to the __init__()

                # method of the class identified by class_name

                self.new(eval(class_name)(**obj_item))

        except:

            pass
