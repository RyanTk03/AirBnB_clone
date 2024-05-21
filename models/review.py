#!/usr/bin/python3
"""
review module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that represent a Review model
    """
    place_id = ""
    user_id = ""
    text = ""
