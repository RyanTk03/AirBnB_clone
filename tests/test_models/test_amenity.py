#!/usr/bin/env python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def checking_for_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_attributes_are_string(self):
        self.assertIs(type(self.amenity.name), str)

    def test_class(self):
        """tests if class exists"""
        self.assertEqual(type(self.amenity), Amenity)

    def test_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_to_dict_output(self):
        """test to_dict method creates a dictionary with proper attrs"""
        test_dict = self.amenity.to_dict()
        self.assertEqual(type(test_dict), dict)
        for attr in self.amenity.__dict__:
            self.assertTrue(attr in test_dict)
        self.assertTrue("__class__" in test_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        s = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(s, str(self.amenity))


if __name__ == "__main__":
    unittest.main()
