#!/usr/bin/python3
"""
The base_model module has the BaseModel class to create instances with
uniquie ids and additional info abdout the creation and update dates
"""


import uuid
from datetime import datetime


class BaseModel:
    """create instances with unique ids and provide methods to serialize it"""
    def __init__(self, *args, **kwargs):
        """initialize  an instance with the following public attributes:
        id : unique universal id
        created_at : creation time and date
        updated_at : update time and date
        but in case kwargs is defined::
        the object will haev all attributes included in the kwargs"""
        if kwargs:
            for item in kwargs.items():
                if item[0] not in ["__class__", "created_at", "updated_at"]:
                    self.__dict__[item[0]] = item[1]
                elif item[0] in ["created_at", "updated_at"]:
                    # 2017-09-28T21:03:54.052302
                    date_list = item[1].split("T")[0].split("-")
                    time_list = item[1].split("T")[1].split(".")[0].split(":")
                    mic_sec = item[1].split("T")[1].split(".")[1]
                    new_datetime = datetime(int(date_list[0]),
                                            int(date_list[1]),
                                            int(date_list[2]),
                                            int(time_list[0]),
                                            int(time_list[1]),
                                            int(time_list[2]),
                                            int(mic_sec))
                    self.__dict__[item[0]] = new_datetime
        else:
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
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
