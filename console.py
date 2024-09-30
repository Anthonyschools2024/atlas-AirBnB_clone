#!/usr/bin/python3
"""Defines the entry point for the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line input."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
