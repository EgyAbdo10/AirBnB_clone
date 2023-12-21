#!/usr/bin/python3


"""this module is the cosole for the hbnb project"""


import cmd
from models.base_model import BaseModel
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
