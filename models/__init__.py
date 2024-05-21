#!/usr/bin/python3
"""
Set the models directory as a module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
