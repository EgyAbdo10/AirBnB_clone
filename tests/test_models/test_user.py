#!/usr/bin/python3

"""this module is teh test suite for the user class"""


from models.user import User
import unittest


class test_user(unittest.TestCase):
    """this class tests the User class"""
    user1 = User()

    def test_email(self):
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertIsInstance(self.user1.email, str)

    def test_password(self):
        self.assertTrue(hasattr(self.user1, "password"))
        self.assertIsInstance(self.user1.password, str)

    def test_first_name(self):
        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertIsInstance(self.user1.first_name, str)

    def test_last_name(self):
        self.assertTrue(hasattr(self.user1, "last_name"))
        self.assertIsInstance(self.user1.last_name, str)
