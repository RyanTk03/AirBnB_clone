#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_instantiation(self):
        """Tests instantiation of State class."""
        b = State()
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))
        self.assertTrue('name' in dir(State))


if __name__ == "__main__":
    unittest.main()
