 #!/usr/bin/env python3
"""
Module of Unittests.
"""
import unittest
import uuid
import datetime
import os
import json
from tests.base_test_case import BaseTestCase 
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
                

class TestFileStorageInstanciation(BaseTestCase):
    """File Storage instanciation success."""

    def test_instance(self):
        """Test file storage engine(object) instantiation."""
        self.assertIsInstance(storage, FileStorage)
        self.assertIn("_FileStorage__file_path", dir(FileStorage()))
        self.assertIn("_FileStorage__objects", dir(FileStorage()))


class TestFileStorageAll(BaseTestCase):
    """File Storage 'all' method test."""

    def test_all_output(self):
        """Test save and reload functions."""
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertIsInstance(obj, dict)


class TestFileStorageNew(BaseTestCase):
    """File Storage 'new' method test."""

    def test_new_object_storage(self):
        """Test 'new' method with new BaseModel instance."""
        store_objs = storage.all()
        size1 = len(store_objs)
        b = BaseModel()
        size2 = len(store_objs)
        self.assertNotEqual(size1, size2)
        self.assertIn('BaseModel.' + b.id, store_objs.keys())
        
    def test_new_object_from_dict_storage(self):
        """Test 'new' method with BaseModel instance from dict."""
        store_objs = storage.all()
        size1 = len(store_objs)
        dict_attrs = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(),
        }
        b = BaseModel(**dict_attrs)
        size2 = len(store_objs)
        self.assertEqual(size1, size2)
        self.assertNotIn('BaseModel.' + b.id, store_objs.keys())

class TestFileStorageSave(BaseTestCase):
    """File storage 'save' method test."""

    def test_save_in_file_storage(self):
        """Test that an object is correctly saved in file storage."""
        b = BaseModel()
        b.save();
        self.assertTrue(os.path.exists(storage.file_path))
        with open(storage.file_path, 'r') as file:
            data = json.load(file)
            self.assertIsNotNone(data)
            self.assertIn("BaseModel." + b.id, data)


class TestFileStorageReload(BaseTestCase):
    """Test cases for the 'reload' method."""

    def test_reload(self):
        """Test if reloading an object stored manually in the storage."""
        try:
            with open(storage.file_path, 'w') as file:
                b = BaseModel()
                objs_to_store = {"BaseModel." + b.id: b.to_dict()}
                json.dump(objs_to_store, file)
            storage.reload()
            self.assertIn("BaseModel." + b.id, storage.all().keys())
        except Exception as e:
            self.fail(e)

    def test_reload_no_exception_if_file_not_exists(self):
        """Test if no exception is rased if there is no file save."""
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
        try:
            storage.reload()
            self.assertTrue(True)
        except FileNotFoundError as e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()

