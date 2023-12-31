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
        arg = arg.strip()
        if arg in self.classes_list:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        elif arg:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        line = line.strip()
        arg_list = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arg_list[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif (
            "{}.{}".format(arg_list[0], 
                           arg_list[1].replace("'", "").replace('"', ''))
            not in storage.all().keys()
        ):
            print("** no instance found **")
        else:
            id = arg_list[1].replace("'", "").replace('"', '')
            obj = storage.all()[f"{arg_list[0]}.{id}"]
            print(obj)

    def do_destroy(self, line):
        line = line.strip()
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
        line = line.strip()
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
        line = line.strip()
        arg_list = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arg_list[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif (
            "{}.{}".format(arg_list[0], arg_list[1].replace('"', "").replace("'", ""))
            not in storage.all().keys()
                ):
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            # delete quotes from attibutre name
            id = arg_list[1].replace('"', "").replace("'", "")
            if '"' in arg_list[3]:
                str_attr_val = arg_list[3].split('"')[1]
            elif "'" in arg_list[3]:
                str_attr_val = arg_list[3].split("'")[1]
            else:
                str_attr_val = arg_list[3]
            # delete quotes from attibutre value
            if '"' in arg_list[2]:
                str_attr_name = arg_list[2].split('"')[1]
            elif "'" in arg_list[2]:
                str_attr_name = arg_list[2].split("'")[1]
            else:
                str_attr_name = arg_list[2]  
            try:
                attr_val = json.loads(str_attr_val)
            except json.decoder.JSONDecodeError:
                attr_val = str_attr_val
            obj = storage.all()[f"{arg_list[0]}.{id}"]
            obj.__dict__[str_attr_name] = attr_val
            obj.save()

    def default(self, line):
        line = line.strip()
        if "." in line:
            cls_name = line.split(".")[0]
            command = line.split(".")[1].split("(")[0]
            id = line.split(".")[1].split("(")[1][:-1]
            if command == "all":
                eval("self.do_" + command)(cls_name)
            elif cls_name in self.classes_list and command == "count":
                co = 0
                for k, v in storage.all().items():
                    if v.__class__.__name__ == cls_name:
                        co += 1
                print(co)
            elif command == "show":
                eval("self.do_" + command)(f"{cls_name} {id}")
            elif command == "destroy":
                eval("self.do_" + command)(f"{cls_name} {id}")
            # <class name>.update(<id>, <attribute name>, <attribute value>)
            # <class name>.update(<id>, <dictionary representation>)
            elif command == "update":
                try:
                    args2 = line.split(".")[1].split("(")[1][:-1]
                    attr_dict_str = args2.split(", {")[1].strip().replace(" ", "")
                    id = args2.split(", {")[0]
                    atrr_dict = json.loads("{" + attr_dict_str.replace("'", '"'))
                    for k, v in atrr_dict.items():
                        eval("self.do_" + command)(f"{cls_name} {id} {k} {v}")
                except:
                    args = line.split(".")[1].split("(")[1][:-1].replace(",", "")
                    eval("self.do_" + command)(f"{cls_name} {args}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

