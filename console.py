#!/usr/bin/python3


"""this module is the cosole for the hbnb project"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """this class is the hbnb console class"""
    prompt = "(hbnb) "

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
        if arg in ["BaseModel"]:
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
        elif arg_list[0] not in ["BaseModel"]:
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
        elif arg_list[0] not in ["BaseModel"]:
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
        else:
            obj_list = (
                [str(val) for val in storage.all().values()
                 if val.__class__.__name__ in arg_list]
            )
        print(obj_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
