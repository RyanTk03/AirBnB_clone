#!/usr/bin/python3
"""
Defines the HBnB console.
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "

    __models_map = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def check_args(self, args, checkId=False):
        """
        Check if the argument passed to the command line are correct
        """
        args_values = parse(args)
        check_success = True
        if len(args_values) == 0:
            print("** class name missing **")
            check_success = False
        elif args_values[0] not in HBNBCommand.__models_map.keys():
            print("** class doesn't exist **")
            check_success = False
        elif checkId and len(args_values) == 1:
            print("** instance id missing **")
            check_success = False
        return (args_values, check_success)

    def emptyline(self):
        """Behavior when receiving an empty line."""
        pass  # Nothing to do

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, args):
        """
        Exit the program.
        """
        print("Bye")
        return True

    def do_EOF(self, args):
        """Exit the program."""
        print("Bye")
        return True

    def do_help(self, args):
        """
        Display help in the console
        """
        super().do_help(args)

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) 
        and prints the id. Ex: (hbnb) create BaseModel
        """
        args_values, check_success = HBNBCommand.check_args(args)
        if check_success:
            new_record = HBNBCommand.__models_map[args_values[0]]()
            new_record.save()
            print(new_record.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class 
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args_values, check_success = HBNBCommand.check_args(args, True)
        objects = storage.all()
        if check_success:
            if "{}.{}".format(args_values[0], args_values[1]) not in objects.keys():
                print("** no instance found **")
            else:
                print(objects["{}.{}".format(args_values[0], args_values[1])])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args_values, check_success = HBNBCommand.check_args(args, True)
        objects = storage.all()
        if check_success:
            if ("{}.{}".format(args_values[0], args_values[1])
                    not in objects.keys()):
                print("** no instance found **")
            else:
                del objects["{}.{}".format(args_values[0], args_values[1])]
                storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all.
        """
        args_values = parse(args)
        if (len(args_values) > 0 and args_values[0]
                not in HBNBCommand.__models_map.key()):
            print("** class doesn't exist **")
        else:
            output = []
            records = storage.all().values()
            for rec in records:
                if len(args_values) > 0 and args_values[0] == rec.__class__.__name__:
                    output.append(rec.__str__())
                elif len(args_values) == 0:
                    output.append(rec.__str__())
            print(output)

    def do_count(self, arg):
        """
        Behavior when retrieving the number of record of a given model.
        """
        args_values, check_success = HBNBCommand.check_args(arg)
        if check_success:
            count = 0
            records = storage.all().values()
            for rec in records:
                if args_values[0] == rec.__class__.__name__:
                    count += 1
            print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or 
        updating attribute (save the change into the JSON file)
        """
        args_values, check_success = HBNBCommand.check_args(arg, True)
        records = storage.all()

        if not check_success:
            return False
        if ("{}.{}".format(args_values[0], args_values[1])
                not in records.keys()):
            print("** no instance found **")
            return False
        if len(args_values) == 2:
            print("** attribute name missing **")
            return False
        if len(args_values) == 3:
            try:
                type(eval(args_values[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        to_update = records["{}.{}".format(args_values[0], args_values[1])]
        if len(args_values) == 4:
            if args_values[2] in to_update.__class__.__dict__.keys():
                valtype = type(to_update.__class__.__dict__[args_values[2]])
                to_update.__dict__[args_values[2]] = valtype(args_values[3])
            else:
                to_update.__dict__[args_values[2]] = args_values[3]
        elif type(eval(args_values[2])) == dict:
            for k, v in eval(args_values[2]).items():
                if (k in to_update.__class__.__dict__.keys() and
                        type(to_update.__class__.__dict__[k]) in
                        {str, int, float}):
                    valtype = type(to_update.__class__.__dict__[k])
                    to_update.__dict__[k] = valtype(v)
                else:
                    to_update.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
