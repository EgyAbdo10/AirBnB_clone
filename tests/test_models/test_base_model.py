#!/usr/bin/python3

"""this module is used for unittesting the base model classs"""


from models.base_model import BaseModel, uuid
import unittest
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """test the base model class methods and attributes"""
    obj1 = BaseModel()

    def test_id_type(self):
        self.assertIsInstance(self.obj1.id, str)

    def test_created_date_type(self):
        self.assertIsInstance(self.obj1.created_at, datetime)

    def test_updated_date_type(self):
        self.assertIsInstance(self.obj1.updated_at, datetime)

    def test_string_method(self):
        self.assertEqual(
            str(self.obj1), f"""[{self.obj1.__class__.__name__}]"""
            f""" ({self.obj1.id}) {self.obj1.__dict__}"""
            )

    def test_save(self):
        self.obj1.save()
        self.assertAlmostEqual(self.obj1.updated_at.timestamp(),
                               datetime.now().timestamp(), 1)

    def test_to_dict_ret_type(self):
        self.assertIsInstance(self.obj1.to_dict(), dict)

    def test_to_dict_ret_val(self):
        key_list = list(self.obj1.__dict__.keys())
        for key in key_list:
            if key not in ["created_at", "updated_at"]:
                self.assertEqual(self.obj1.__dict__[key],
                                 self.obj1.to_dict()[key])

        self.assertEqual(self.obj1.__class__.__name__,
                         self.obj1.to_dict()["__class__"])
        self.assertEqual(self.obj1.created_at.isoformat(),
                         self.obj1.to_dict()["created_at"])
        self.assertEqual(self.obj1.updated_at.isoformat(),
                         self.obj1.to_dict()["updated_at"])

    def test_kwargs_init(self):
        # kwargs has all needed attributes
        obj2 = BaseModel(**self.obj1.to_dict())
        self.assertEqual(obj2.__dict__, self.obj1.__dict__)
        self.assertNotEqual(obj2, self.obj1)
        # kwargs has no attribute
        obj2 = BaseModel()
        attrs = ["__class__", "created_at", "updated_at"]
        [self.assertTrue(hasattr(obj2, attr)) for attr in attrs]
