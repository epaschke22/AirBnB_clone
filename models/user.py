#!/usr/bin/python3
"""User Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """class to represent users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
