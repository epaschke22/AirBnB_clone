#!/usr/bin/python3
"""Base Model"""
import uuid
import datetime
from models import storage


class BaseModel:
    """Base class for all objects"""
    def __init__(self, *args, **kwargs):
        """init"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new()
        else:
            for key in kwargs.keys():
                if key is "__class__":
                    continue
                elif key is "created_at" or key is "updated_at":
                    setattr(self, key,
                            datetime.datetime.strptime
                            (kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """returns string about object"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates object"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary of object"""
        output = self.__dict__
        output["created_at"] = self.created_at.isoformat()
        output["updated_at"] = self.updated_at.isoformat()
        output["__class__"] = type(self).__name__
        return output
