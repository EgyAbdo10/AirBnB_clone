#!/usr/bin/python3

"""this module tests the amenity module"""

from models.amenity import Amenity
import unittest


class test_amenity(unittest.TestCase):
    """this class is the test suite for the amenity class"""
    amenity1 = Amenity()

    def test_amenity_name(self):
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertIsInstance(self.amenity1.name, str)
