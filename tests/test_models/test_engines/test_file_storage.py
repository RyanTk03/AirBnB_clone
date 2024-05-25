#!/usr/bin/env python3
"""
Module of Unittests
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ File Storage Tests """


    def test_class_instance(self):
        """ Test instance """
        self.assertIsInstance(storage, FileStorage)

    def test_save(self):
        """ Test save and reload functions """
        test_model = BaseModel()
        tmp_createdAt = test_model.created_at
        test_model.save()
        model_dict = test_model.to_dict()
        objs = storage.all()
        key = "BaseModel." + test_model.id
        self.assertEqual(objs[key].created_at, tmp_createdAt)

    def test_attributes(self):
        """Test if attributes exist"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_reload(self):
        """Test if reloading"""
        test_model = BaseModel()
        objs = storage.all()
        test_model.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(objs, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(objs[key].to_dict(), value.to_dict())

    def test_reload_saving(self):
        """Test save"""
        test_model = BaseModel()
        tmp_createdAt = test_model.created_at
        key = "BaseModel." + test_model.id
        test_model.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        storage.reload()
        objs = storage.all()
        self.assertEqual(objs[key].created_at, tmp_createdAt)


if __name__ == '__main__':
    unittest.main()

