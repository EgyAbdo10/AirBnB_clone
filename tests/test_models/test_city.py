#!/usr/bin/python3

"""this module tests the city module"""

from models.city import City
import unittest


class test_state(unittest.TestCase):
    """this class is teh test suite for the State class"""
    city1 = City()

    def test_city_name(self):
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertIsInstance(self.city1.name, str)

    def test_city_state_id(self):
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertIsInstance(self.city1.state_id, str)
