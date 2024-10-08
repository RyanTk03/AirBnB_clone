#!/usr/bin/python3
"""
Defines a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import os
import json


class FileStorage:
    """A class used to serialize and deserialize data stored in JSON file"""
    __file_path = "data/file.json"
    __objects = {}

    @property
    def file_path(self):
        return FileStorage.__file_path

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects[str(class_name) + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        items = FileStorage.__objects.items()
        record = {key: value.to_dict() for key, value in items}
        with open(FileStorage.__file_path, mode='w', encoding="UTF-8") as f:
            json.dump(record, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.exists(FileStorage.__file_path):
            return
        try:
            enc = "UTF-8"
            with open(FileStorage.__file_path, mode='r', encoding=enc) as f:
                data = json.load(f)
                if data is None:
                    return
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                models = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
                }
                for key, val in data.items():
                    model_name, model_id = key.split('.')
                    instance = models[model_name](**val)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            FileStorage.__objects = {}
            print("storage file not found")
        except json.JSONDecodeError:
            FileStorage.__objects = {}
            print("JSON decoding error: The file may be corrupted or \
malformed.")
