#!/usr/bin/python3
"""
Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBase_Instance_Print
    TestBaseModel_save
    TestBase_from_json_string
    TestBaseModel_to_dict
"""
from fileinput import lineno
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import time
import uuid
import json
import os


class TestBaseModel_NewObject(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        """Set up unitest properties"""
        self.longMessage = True

    def test_is_instance_of(self):
        """Test instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(str(type(b1)), str(BaseModel))

    def test_default_attributes(self):
        """Test that default attribute exists"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"), "'id' shoud exists in a BaseModel \
                object instantiate without kwargs")
        self.assertTrue(hasattr(b1, "created_at"), "'created_at' should \
                exists in a BaseModel object instantiate without kwargs")
        self.assertTrue(hasattr(b1, "updated_at"), "'updated_at' should \
                exists in a BaseModel object instantiate without kwargs")
        self.assertIsInstance(b1.id, str, "'id' should be a string")
        self.assertIsInstance(b1.created_at, datetime, "'created_at' should \
                be an instance of datetime")
        self.assertIsInstance(b1.updated_at, datetime, "'updated_at' should \
                be an instance of datetime")

    def test_kwargs_attributes(self):
        dt = datetime.now()
        b1 = BaseModel(id="345", created_at=dt, updated_at=dt)
        self.assertEqual(b1.id, "345")
        self.assertEqual(b1.created_at, dt)
        self.assertEqual(b1.updated_at, dt)

    def test_compare_instances_id(self):
        """Compare distinct instances ids"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_instantiation_with_none_kwargs(self):
        b1 = BaseModel(id=None, created_at=None, updated_at=None)
        self.assertIsNotNone(b1.id, "'id' should not be None even if value \
                in kwargs is None")
        self.assertIsNotNone(b1.created_at, "'created_at' should not be None \
                even if value in kwargs is None")
        self.assertIsNotNone(b1.updated_at, "'updated_at' should not be None \
                even if value in kwargs is None")


class TestBaseModel_str_method(unittest.TestCase):
    """Unittest for testing the __str__ method."""

    def test_str(self):
        """test that the str method has the correct output"""
        b1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(b1.id, b1.__dict__)
        self.assertEqual(string, str(b1))


class TestBaseModel_save_method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        """Check save models"""
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_save_with_arg(self):
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.save(None)

    def test_save(self):
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)


class TestBaseModel_to_dict_method(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def test_to_dict(self):
        """Test if the to_dict method exists"""
        b = BaseModel()
        self.assertTrue('to_dict' in dir(b))

    def test_to_dict_value(self):
        """Test output of to_dict method"""
        b1 = BaseModel()
        b1_id = b1.id
        b1_updatedAt = b1.updated_at.isoformat()
        b1_createdAt = b1.created_at.isoformat()
        b1_to_dict = b1.to_dict()
        test_dict = {
            "id": b1_id,
            "__class__": "BaseModel",
            "created_at": b1_createdAt,
            "updated_at": b1_updatedAt
        }
        self.assertEqual(dict, type(b1_to_dict))  # test to_dict output type
        self.assertDictEqual(b1_to_dict, test_dict)  # test to_dict output
        self.assertNotEqual(b1_to_dict, b1.__dict__)  # output =! __dict__
        self.assertIn("id", b1_to_dict)
        self.assertIn("created_at", b1_to_dict)
        self.assertIn("updated_at", b1_to_dict)
        self.assertIn("__class__", b1_to_dict)

    def test_to_dict_type(self):
        """Test datetime field isoformated"""
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)

    def test_to_dict_contains_added_attributes(self):
        b = BaseModel()
        b.test_name = "Holberton"
        b.test_number = 98
        self.assertEqual("Holberton", b.test_name)
        self.assertIn("test_number", b.to_dict())


if __name__ == "__main__":
    unittest.main()
