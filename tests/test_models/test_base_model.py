#!/usr/bin/python3
"""
Defines unittests for models/base_model.py.
"""
import unittest
import datetime
import time
from models.base_model import BaseModel
from tests.base_test_case import BaseTestCase


class TestBaseModelInstantiation(BaseTestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.b = BaseModel()

    def util_test_type(self, instance):
        """Util that test the type of an instance attributes"""
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_is_instance_of_base_model(self):
        """Test that an instance was created with the right class."""
        self.assertIsInstance(self.b, BaseModel)

    def test_instance_default_attributes(self):
        """Test that default attributes exist."""
        self.assertTrue(hasattr(self.b, "id"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))

    def test_instance_attributes_types(self):
        """Test that attributes are of the correct type."""
        self.util_test_type(self.b)

    def test_instance_kwargs_attributes(self):
        """Test named attributes are correctly created."""
        dt = datetime.datetime.now()
        b1 = BaseModel(id="345", created_at=dt, updated_at=dt)
        self.assertEqual(b1.id, "345")
        self.assertEqual(b1.created_at, dt)
        self.assertEqual(b1.updated_at, dt)
        self.util_test_type(b1)

    def test_unique_instances_ids(self):
        """Test id uniqueness for multiple distinct instances."""
        bms = [BaseModel() for i in range(0, 100)]
        ids = [b.id for b in bms]
        unique_ids = set(ids)
        self.assertEqual(len(ids), len(unique_ids))

    def test_instantiation_with_none_kwargs(self):
        """Test that the None value are handled."""
        b1 = BaseModel(id=None, created_at=None, updated_at=None)
        self.assertIsNotNone(b1.id, "'id' should not be None even if value \
                in kwargs is None")
        self.assertIsNotNone(b1.created_at, "'created_at' should not be None \
                even if value in kwargs is None")
        self.assertIsNotNone(b1.updated_at, "'updated_at' should not be None \
                even if value in kwargs is None")


class TestBaseModelStr(BaseTestCase):
    """Unittest for testing the __str__ method."""

    def test_str(self):
        """test that the __str__ method has the correct output."""
        b = BaseModel()
        expected = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(expected, str(b))


class TestBaseModelSave(BaseTestCase):
    """Unittest for testing the save method."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.b = BaseModel()

    def test_save_exists(self):
        """Test if the save method exists."""
        self.assertTrue(hasattr(self.b, 'save'))

    def test_attributes_updated_at(self):
        """Test if th attributes updated_at was updated."""
        last_updated = self.b.updated_at.replace()
        time.sleep(1.5)
        self.b.save()
        new_updated = self.b.updated_at.replace()
        self.assertNotEqual(last_updated, new_updated)


class TestBaseModelToDict(BaseTestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def setUp(self):
        """Set up the test case with a base madel"""
        self.b = BaseModel()

    def test_to_dict_exists(self):
        """Test if the to_dict method exists."""
        self.assertTrue(hasattr(self.b, 'to_dict'))

    def test_to_dict_output_attribut(self):
        """Test the contain of the output of to_dict method."""
        to_dict_result = self.b.to_dict()
        self.assertIn("id", to_dict_result)
        self.assertIn("created_at", to_dict_result)
        self.assertIn("updated_at", to_dict_result)
        self.assertIn("__class__", to_dict_result)

    def test_to_dict_value(self):
        """Test the value output of to_dict method."""
        updated_at = self.b.updated_at.isoformat()
        created_at = self.b.created_at.isoformat()
        to_dict_result = self.b.to_dict()
        to_dict_expected = {
            "id": self.b.id,
            "__class__": "BaseModel",
            "created_at": created_at,
            "updated_at": updated_at
        }
        self.assertIsInstance(to_dict_result, dict)  # test to_dict output type
        self.assertNotEqual(to_dict_result, self.b.__dict__) # instance not e
        self.assertDictEqual(to_dict_result, to_dict_expected)

    def test_to_dict_type(self):
        """Test datetime field isoformated."""
        to_dict_result = self.b.to_dict()
        self.assertIsInstance(to_dict_result["created_at"], str)
        self.assertIsInstance(to_dict_result["updated_at"], str)
        self.assertIsInstance(to_dict_result["id"], str)

    def test_to_dict_contains_added_attributes(self):
        """Test that test that to_dict return new attributes."""
        self.b.test_name = "Holberton"
        to_dict_result = self.b.to_dict()
        self.assertIn("test_name", to_dict_result)
        self.assertEqual("Holberton", to_dict_result["test_name"])


if __name__ == "__main__":
    unittest.main()
