#!/usr/bin/python3

"""this module is the test suite for the engine package"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os
import json


class test_FileStorage(unittest.TestCase):
    """test the FileStorage class's methods and attributes"""
    obj1 = BaseModel()
    obj1.save()
    obj2 = BaseModel()
    obj2.save()
    file_path = "/home/egyabdo/AirBnB_clone/file.json"

    def test_save(self):
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            objects = json.load(f)
        self.assertEqual(
                self.obj1.to_dict(),
                objects[self.obj1.__class__.__name__ + "." + str(self.obj1.id)]
        )

    def test_all(self):
        with open(self.file_path, "r") as f:
            objects = json.load(f)
        self.assertEqual(objects, storage.all())

    def test_reload(self):
        storage.reload()
        with open(self.file_path, "r") as f:
            objects = json.load(f)
        self.assertEqual(objects, storage.all())

    def test_new(self):
        new_obj = BaseModel()
        new_obj.age = 18
        storage.new(new_obj)
        objects = storage.all()
        self.assertEqual(
              objects[new_obj.__class__.__name__ + "." + str(new_obj.id)],
              new_obj.to_dict()
        )
