#!/usr/bin/python3

"""this module has the FileStorage class which performs operations
on the storage file"""


import json
from models.base_model import BaseModel
import os


class FileStorage:
    """perform operations on the storage files"""
    __file_path = ""
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
