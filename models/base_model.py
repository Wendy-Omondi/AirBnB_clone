#!/usr/bin/python3
"""defines a BseModel class"""
import models
from uuid import uuid4
from datetime import datetime
# from models.__init__ import storage
# from models.engine.file_storage import FileStorage


class BaseModel:
    """defines all common attributes/methods of other classes"""

    def __init__(self, *args, **kwargs):
        """
        method to instantate an instance of BaseModel
        """
        def args(self):
            pass
        self.id = str(uuid4())          
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of __dict__ of the instance
        """
        return{
                'id': self.id,
                'created_at':
                str(self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')),
                'updated_at':
                str(self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')),
                }

    def __str__(self):
        """prints the class name, id and dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

