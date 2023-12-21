#!/usr/bin/python3

"""this module has the Review class to create Reviews"""


from models.base_model import BaseModel


class Review(BaseModel):
    """this class creates Review instances"""
    place_id = ""
    user_id = ""
    text = ""
