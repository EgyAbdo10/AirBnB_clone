#!/usr/bin/python3

"""this module is the test suite for the Place class"""


import unittest
from models.place import Place


class test_place(unittest.TestCase):
    """this class is a test case for the Place class"""
    place1 = Place()

    def test_place_name(self):
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertIsInstance(self.place1.name, str)

    def test_city_id(self):
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertIsInstance(self.place1.city_id, str)

    def test_user_id(self):
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertIsInstance(self.place1.user_id, str)

    def test_description(self):
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertIsInstance(self.place1.description, str)

    def test_number_rooms(self):
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertIsInstance(self.place1.number_rooms, int)

    def test_number_batroom(self):
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertIsInstance(self.place1.number_bathrooms, int)

    def test_max_guest(self):
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertIsInstance(self.place1.max_guest, int)

    def test_price_by_night(self):
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertIsInstance(self.place1.price_by_night, int)

    def test_latitude(self):
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertIsInstance(self.place1.latitude, float)

    def test_longitude(self):
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertIsInstance(self.place1.longitude, float)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.place1, "amenity_ids"))
        self.assertIsInstance(self.place1.amenity_ids, list)
