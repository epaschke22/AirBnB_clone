#!/usr/bin/python3
"""Base Model"""
import uuid
import datetime

class BaseModel:
    """Base class for all objects"""
    def __init__(self, *args, **kwargs):
        """init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        for key in kwargs.keys():
            if key is "__class__":
                continue
            elif key is "created_at" or key is  "updated_at":
                setattr(self, key, datetime.datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'))
            else:
                setattr(self, key, kwargs[key])

    def __str__(self):
        """returns string about object"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates object"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns dictionary of object"""
        output = self.__dict__
        output["created_at"] = self.created_at.isoformat()
        output["updated_at"] = self.updated_at.isoformat()
        output["__class__"] = "BaseModel"
        return output

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--")
print(my_model is my_new_model)
