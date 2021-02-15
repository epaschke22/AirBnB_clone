#!/usr/bin/python3
"""Base Model"""
import uuid
import datetime
import models


class BaseModel:
    """Base class for all objects"""
    def __init__(self, *args, **kwargs):
        """init"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """returns string about object"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates object"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary of object"""
        output = dict(self.__dict__)
        output["created_at"] = self.created_at.isoformat()
        output["updated_at"] = self.updated_at.isoformat()
        output["__class__"] = type(self).__name__
        return output
