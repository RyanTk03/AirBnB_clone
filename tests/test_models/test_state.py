#!/usr/bin/python3
"""Defines unittests for models/state.py.
Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models import storage
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
