#!/usr/bin/python3


"""this module is the cosole for the hbnb project"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """this class is the hbnb console class"""
    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program when EOF occurs"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if arg in self.classes_list:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        elif arg:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        arg_list = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arg_list[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif (
            f"{arg_list[0]}.{arg_list[1]}" not in storage.all().keys()
        ):
            print("** no instance found **")
        else:
            obj = storage.all()[f"{arg_list[0]}.{arg_list[1]}"]
            print(obj)

    def do_destroy(self, line):
        arg_list = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arg_list[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif (
            f"{arg_list[0]}.{arg_list[1]}" not in storage.all().keys()
        ):
            print("** no instance found **")
        else:
            storage._FileStorage__objects.__delitem__(
                f"{arg_list[0]}.{arg_list[1]}"
            )
            storage.save()

    def do_all(self, line):
        arg_list = line.split(" ")
        if line == "":
            obj_list = (
                [str(val) for val in storage.all().values()]
            )
            print(obj_list)

        elif line not in self.classes_list:
            print("** class doesn't exist **")
        else:
            obj_list = (
                [str(val) for val in storage.all().values()
                 if val.__class__.__name__ == line]
            )
            print(obj_list)

    def do_update(self, line):
        arg_list = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arg_list[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif (
            f"{arg_list[0]}.{arg_list[1]}" not in storage.all().keys()
                ):
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            if '"' in arg_list[3]:
                str_attr_val = line.split('"')[1]
            else:
                str_attr_val = arg_list[3]
            try:
                attr_val = json.loads(str_attr_val)
            except json.decoder.JSONDecodeError:
                attr_val = str_attr_val
            obj = storage.all()[f"{arg_list[0]}.{arg_list[1]}"]
            obj.__dict__[arg_list[2]] = attr_val
            obj.save()

    def default(self, line):
        if "." in line:
            cls_name = line.split(".")[0]
            command = line.split(".")[1].split("(")[0]
            if cls_name in self.classes_list and command == "all":
                eval("self.do_" + command)(cls_name)
            elif cls_name in self.classes_list and command == "count":
                co = 0
                for k, v in storage.all().items():
                    if v.__class__.__name__ == cls_name:
                        co += 1
                print(co)
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
