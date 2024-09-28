#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        """Set up unitest properties"""
        self.longMessage = True

    def test_is_instance_of(self):
        """Test instance"""
        u = User()
        self.assertIsInstance(u, User)
        self.assertEqual(str(type(u)), str(User))
        self.assertTrue(issubclass(type(u), User))

    def test_str(self):
        """test that the str method has the correct output"""
        u = User()
        string = "[User] ({}) {}".format(u.id, u.__dict__)
        self.assertEqual(string, str(u))

    def test_email(self):
        """Test that User has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """Test that User has attr password, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """Test that User has attr first_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """Test that User has attr last_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_to_dict_output(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        test_dict = u.to_dict()
        self.assertEqual(type(test_dict), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in test_dict)
        self.assertTrue("__class__" in test_dict)


if __name__ == "__main__":
    unittest.main()
