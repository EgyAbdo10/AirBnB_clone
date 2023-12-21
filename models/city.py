#!/usr/bin/python3

"""this module has the City class to create city instances"""


from models.base_model import BaseModel


class City(BaseModel):
    """this class creates City instances"""
    state_id = ""
    name = ""
