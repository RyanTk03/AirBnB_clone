#!/usr/bin/env python3
"""Test model for Review class
"""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petesburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        self.assertEqual(type(self.review), Review)
        self.assertTrue(issubclass(type(self.review), BaseModel))
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_type(self):
        self.assertIs(type(self.review.user_id), str)
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.text), str)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.review))

    def test_to_dict_output(self):
        """test to_dict method creates a dictionary with proper attrs"""
        test_dict = self.review.to_dict()
        self.assertEqual(type(test_dict), dict)
        for attr in self.review.__dict__:
            self.assertTrue(attr in test_dict)
        self.assertTrue("__class__" in test_dict)

    def test_str(self):
        """test that the str method has the correct output"""
        s = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(s, str(self.review))


if __name__ == "__main__":
    unittest.main()
