#!/usr/bin/python3
"""File Storage"""
import json


class FileStorage:
    """engie to store and load files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the contents of dictionary __objects"""
        return __objects

    def new(self, obj):
        """adds new object to the __object dict"""
        string = obj.__class__.__name__ + '.' + obj.id
        self.__objects[string] = obj.to_dict()

    def save(self):
        """serializes or saves the __objects dict into a json file"""
        with open(__file_path, 'w') as file:
            file.write(json.dumps(__objects))

    def reload(self):
        """turns the json file back into the __objects dict"""
        try:
            with open(__file_path) as file:
                __objects = json.loads(file.read())
        except:
            pass
