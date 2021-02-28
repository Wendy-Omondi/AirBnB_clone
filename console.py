#!/usr/bin/python3
"""contains entry point of the command interprator"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from shlex import split
import json


class HBNBCommand(cmd.Cmd):
    """class definition"""
    doc_header = '(Documented commands (type help <topic>):)'
    prompt = ' (hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, line):
        """An end-of-file on input is passed back as the string EOF"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """override default emptyline"""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        arg = parse(args)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.

        """
        o_dic = storage.all
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in o_dic:
            print("** no instance found **")
        else:
            print(o_dic["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Deletes an instance base on the case name and id"""
        o_dic = storage.all
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in o_dic.keys():
            print("** no instance found **")
        else:
            del o_dic["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
           based or not on the class name.
        """
        if len(arg) > 0 and arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for ob in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    obj.append(ob.__str__())
                elif len(arg) == 0:
                    obj.append(ob.__str__())
            print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
           adding or updating attribute
        """
        o_dic = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        if len(arg) == 1:
            print("** instance id missing **")
        if "{}.{}".format(argl[0], argl[1]) not in o_dic.keys():
            print("** no instance found **")
        if len(arg) == 2:
            print("** attribute name missing **")
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        storage.save()


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
