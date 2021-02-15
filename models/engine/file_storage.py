#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """engie to store and load files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the contents of dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds new object to the __object dict"""
        string = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[string] = obj

    def save(self):
        """serializes or saves the __objects dict into a json file"""
        output = {}
        for key, value in FileStorage.__objects.items():
            output[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(output, file)

    def reload(self):
        """turns the json file back into the __objects dict"""
        from_json = {}
        try:
            with open(FileStorage.__file_path) as file:
                from_json = json.load(file)
            for key, value in from_json.items():
                if value["__class__"] == "BaseModel":
                    from_json[key] = BaseModel(**value)
                elif value["__class__"] == "User":
                    from_json[key] = User(**value)
                elif value["__class__"] == "State":
                    from_json[key] = State(**value)
                elif value["__class__"] == "City":
                    from_json[key] = City(**value)
                elif value["__class__"] == "Amenity":
                    from_json[key] = Amenity(**value)
                elif value["__class__"] == "Place":
                    from_json[key] = Place(**value)
                elif value["__class__"] == "Review":
                    from_json[key] = Review(**value)
            FileStorage.__objects = from_json
        except:
            pass
