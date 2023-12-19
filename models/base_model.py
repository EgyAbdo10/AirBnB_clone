#!/usr/bin/python3
"""
The base_model module has the BaseModel class to create instances with
uniquie ids and additional info abdout the creation and update dates
"""


import uuid
from datetime import datetime


class BaseModel:
    """create instances with unique ids and provide methods to serialize it"""
    def __init__(self):
        """initialize  an instance with the following public attributes:
        id : unique universal id
        creation time and date
        update time and date"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an object with the follwoing format:
        [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """set the update date to now"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """get the dictionary representation of an object
        the dictionary includes:
        1- all attribute set to an object
        2- the class name of an object
        3- the creation and update dates in iso format
        """
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
