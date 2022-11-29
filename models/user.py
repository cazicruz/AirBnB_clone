#!/usr/bin/python3
"""A module that contains user class"""
from models.base_model import BaseModel


class User(BaseModel):

    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
