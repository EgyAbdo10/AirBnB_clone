#!/usr/bin/python3


"""this module is the cosole for the hbnb project"""


import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
