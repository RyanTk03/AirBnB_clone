#!/usr/bin/env python3
"""Test model for Place class"""

import unittest
import os
from models.place import Place
import uuid


class TestPlace(unittest.TestCase):
    """Place model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.place = Place()
        cls.place.city_id = str(uuid.uuid4())
        cls.place.user_id = str(uuid.uuid4())
        cls.place.name = "Any place in the world"
        cls.place.description = "Suny Beatch"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_instance_of(self):
        """Test instance"""
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertEqual(type(p), Place)
        self.assertTrue(issubclass(type(p), Place))

    def test_str(self):
        """test that the str method has the correct output"""
        p = Place()
        string = "[Place] ({}) {}".format(p.id, p.__dict__)
        self.assertEqual(string, str(p))

    def checking_for_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

    def test_to_dict_output(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        test_dict = p.to_dict()
        self.assertEqual(type(test_dict), dict)
        for attr in p.__dict__:
            self.assertTrue(attr in test_dict)


if __name__ == "__main__":
    unittest.main()
