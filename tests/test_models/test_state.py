#!/usr/bin/python3

"""this module tests the state module"""

from models.state import State
import unittest


class test_state(unittest.TestCase):
    """this class is the test suite for the State class"""
    state1 = State()

    def test_state_name(self):
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertIsInstance(self.state1.name, str)
