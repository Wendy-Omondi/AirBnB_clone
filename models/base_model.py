#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods of other classes"""

    def __init__(self, *args, **kwargs):
        """
        method to instantate an instance of BaseModel
        """
        def args(self):
            pass

        for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = self.created_at

    def __str__(self):
        return ("[<class name>] (<self.id>) <self.__dict__>")

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
