#!/usr/bin/python3
"""
Class user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that represent a User model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
