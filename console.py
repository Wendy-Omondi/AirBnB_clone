#!/usr/bin/python3
"""contains entry point of the command interprator"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class definition"""
    doc_header = '(Documented commands (type help <topic>):)'
    prompt = ' (hbnb) '
    file = None

    def do_EOF(self, line):
        """
        An end-of-file on input is passed back as the string 'EOF'
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        quit(*parse(arg))

    def emptyline(self):
        pass


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
