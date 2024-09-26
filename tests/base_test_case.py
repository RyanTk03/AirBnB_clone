#!/usr/bin/python3
"""Base test case that will clean up file storage after all test."""
import unittest
import os
import json
from models import storage


class BaseTestCase(unittest.TestCase):
    """Define base set up and tear down method for all test."""

    def tearDown(self):
        """Clean up file storage after all test executed."""
        if (os.path.exists(storage.file_path)):
            with open(storage.file_path, 'w') as file:
                json.dump({}, file)