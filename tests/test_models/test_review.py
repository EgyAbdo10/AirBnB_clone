#!/usr/bin/python3

"""this module tests the review module"""

from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """this class is the test suite for the review class"""
    review1 = Review()

    def test_place_id(self):
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertIsInstance(self.review1.place_id, str)

    def test_user_id(self):
        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertIsInstance(self.review1.user_id, str)

    def test_text(self):
        self.assertTrue(hasattr(self.review1, "text"))
        self.assertIsInstance(self.review1.text, str)
