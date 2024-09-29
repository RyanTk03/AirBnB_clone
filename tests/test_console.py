#!/usr/bin/python3
"""Tests case for the console."""
import unittest
from unittest.mock import patch
from io import StringIO
from test_models.test_base_model import BaseTestCase
from models.base_model import BaseModel
from console import HBNBCommand
from models import storage


class TestHBNBCommand(BaseTestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.b = BaseModel()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test creating a BaseModel without class name."""
        HBNBCommand().onecmd("create")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_nonexistent_class(self, mock_stdout):
        """Test creating a nonexistent class."""
        HBNBCommand().onecmd("create MyModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_base_model(self, mock_stdout):
        """Test creating a BaseModel instance."""
        HBNBCommand().onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)

        all_objs = storage.all()
        self.assertIn("BaseModel.{}".format(output), all_objs)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test showing an instance of missing class."""
        HBNBCommand().onecmd("show")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_nonexistent_class(self, mock_stdout):
        """Test showing an instance of nonexistent class."""
        HBNBCommand().onecmd("show MyModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        """Test showing a class instance without provide id."""
        HBNBCommand().onecmd("show BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_nonexistent_instance(self, mock_stdout):
        """Test showing a nonexistent instance of BaseModel."""
        HBNBCommand().onecmd("show BaseModel 12345")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_existent_instance(self, mock_stdout):
        """Test showing an existent instance of BaseModel."""
        HBNBCommand().onecmd("show BaseModel " + self.b.id)
        output = mock_stdout.getvalue().strip()
        expected = storage.all()["BaseModel.{}".format(self.b.id)]
        self.assertEqual(output, str(expected))

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test destroying an instance without class name."""
        HBNBCommand().onecmd("destroy")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_nonexistent_class(self, mock_stdout):
        """Test destroying a nonexistent class."""
        HBNBCommand().onecmd("destroy MyModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test destroying a class instance without providing an id."""
        HBNBCommand().onecmd("destroy BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_nonexistent_instance(self, mock_stdout):
        """Test destroying a nonexistent instance of BaseModel."""
        HBNBCommand().onecmd("destroy BaseModel 121212")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test retrieving all instances."""
        HBNBCommand().onecmd("all")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output, str(storage.all()))

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_nonexistent_class(self, mock_stdout):
        """Test retrieving all instances of a nonexistent class."""
        HBNBCommand().onecmd("all MyModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test updating an instance without class name."""
        HBNBCommand().onecmd("update")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_nonexistent_class(self, mock_stdout):
        """Test updating a nonexistent class."""
        HBNBCommand().onecmd("update MyModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test updating a class instance without providing an id."""
        HBNBCommand().onecmd("update BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attribute_name(self, mock_stdout):
        """Test updating an instance without providing an attribute name."""
        HBNBCommand().onecmd("update BaseModel " + self.b.id)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** attribute name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        """Test updating an instance without providing a value."""
        HBNBCommand().onecmd("update BaseModel {} email".format(self.b.id))
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** value missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_nonexistent_instance(self, mock_stdout):
        """Test updating a nonexistent instance of BaseModel."""
        HBNBCommand().onecmd("update BaseModel 121212 email \"test@ex.com\"")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_existent_instance(self, mock_stdout):
        """Test updating an existent instance of BaseModel."""
        HBNBCommand().onecmd("create User")
        instance_id = mock_stdout.getvalue().strip()

        HBNBCommand().onecmd("update User {} first_name \"NewName\""
                             .format(instance_id))

        all_objs = storage.all()
        updated_instance = all_objs["User.{}".format(instance_id)]
        self.assertEqual(updated_instance.first_name, "NewName")

if __name__ == '__main__':
    unittest.main()
