#!/usr/bin/python3
"""Review Model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class to represent reviews"""
    place_id = ""
    user_id = ""
    text = ""
