#!/usr/bin/python3

"""this module has the user class to craete user instances"""


from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
