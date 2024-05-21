#!/usr/bin/env python3
"""
Module base_model that implements the BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        """

        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    fmt = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, fmt))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a readable state/representation of the model
        """
        name = self.__class__.name
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        Uptade the necessary attribute and save the model in the storage
        """
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """
        Return a dictionnary of key/value of the attribute of the model
        """
        output = self.__dict__.copy()
        output["created_at"] = self.created_at.isoformat()
        output["updated_at"] = self.updated_at.isoformat()
        output["__class__"] = self.__class__.__name__
        return output
