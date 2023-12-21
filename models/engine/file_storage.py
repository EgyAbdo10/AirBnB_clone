#!/usr/bin/python3

"""this module has the FileStorage class which performs operations
on the storage file"""


import json
import os


class FileStorage:
    """perform operations on the storage files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ +
                              "." + str(obj.id)] = obj

    def save(self):
        objects = FileStorage.__objects
        objects_dict = {key: val.to_dict() for key, val in objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..amenity import Amenity
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)

            for key in objects.keys():
                cls_name = objects[key]["__class__"]
                objects[key] = eval(cls_name)(**objects[key])
            FileStorage.__objects = objects
