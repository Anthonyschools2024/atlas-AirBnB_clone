#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter
of the HBNB project. The interpreter manages the following commands:
- quit: Exit the command interpreter.
- EOF: Exit the command interpreter using Ctrl+D.
- create: Creates a new instance of a class.
- show: Prints the string representation of an instance.
- all: Prints all string representations of instances.
- destroy: Deletes an instance.
- update: Updates an instance by adding or updating attributes.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place   
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing objects"""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line + ENTER"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel or other classes"""
        if not arg:
            print("** class name missing **")
            return
        if arg in self.classes:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        objs = storage.all()
        obj_list = []
        if not arg:
            for obj in objs.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif arg in self.classes:
            for key, obj in objs.items():
                if key.startswith(arg):
                    obj_list.append(str(obj))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
