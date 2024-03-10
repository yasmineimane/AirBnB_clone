#!/usr/bin/python3

"""
Module for the parent class BaseModel.
"""

import datetime
import uuid
import models

class BaseModel:
    """
    Super class
    id(str)
    created_at(str)
    updated_at(str)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attribute.
        """

        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and len (kwargs) != 0:
            for l, m in kwargs.items():
                if l == "created_at" or l == "updated_at":
                    self.__dict__[l] = datetime.datetime.strptime(m, tformat)
                else:
                    self.__dict__[l] = m;
            if "id" not in kwargs.keys():
                self.id = f"{uuid.uuid4()}"
        else:
            self.id = f"{uuis.uuid4()}"
            slef.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """
        update the instance updated_at
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary from an instance.
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created.isoformat()
        my_dict["id"] = self.id
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
