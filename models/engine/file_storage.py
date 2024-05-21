#!/usr/bin/python3
"""
Defines a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class used to serialize and deserialize data stored in JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        items = FileStorage.__objects.items()
        record = {key: value.to_dict for key, value in items}
        with open(FileStorage.__file_path, mode='w', encoding="UTF-8") as f:
            json.dump(record, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding="UTF-8") as f:
                data = json.loads(f)
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
                    model = models[model_name](**val)
                    FileStorage.__objects[key] = model
        except FileNotFoundError:
            pass

