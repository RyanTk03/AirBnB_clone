#!/usr/bin/python3
"""Unittest module for the City Class.
"""

import unittest
import uuid
from models.city import City
import os
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """City model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.city = City()
        cls.city.state_id = str(uuid.uuid4())
        cls.city.name = "St. Petesburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_str(self):
        """test that the str method has the correct output"""
        string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(string, str(self.city))

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.city))

    def test_to_dict_output(self):
        """test to_dict method creates a dictionary with proper attrs"""
        test_dict = self.city.to_dict()
        self.assertEqual(type(test_dict), dict)
        for attr in self.city.__dict__:
            self.assertTrue(attr in test_dict)
        self.assertTrue("__class__" in test_dict)


if __name__ == "__main__":
    unittest.main()
