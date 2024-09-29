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

    def hbnb_parse_line(self, line):
        has_bracket = re.search(r"\((.*?)\)", line)
        result = line

        if has_bracket is not None:
            has_curly_bracket = re.search(r"\{(.*?)\}", line)
            if has_curly_bracket is None:
                parsed_list = line[:has_bracket.span()[1] - 1]
                parsed_list = split(parsed_list.replace('.', ' ').
                                    replace('(', ' '))
                parsed_list[0], parsed_list[1] = parsed_list[1], parsed_list[0]
                result = ' '.join(parsed_list)
            else:
                parsed_list = line[:has_curly_bracket.span()[0]]
                parsed_list = split(parsed_list.replace('.', ' ').
                                    replace('(', ' ').strip(', '))
                parsed_list[0], parsed_list[1] = parsed_list[1], parsed_list[0]
                result = ' '.join(parsed_list)
                s_dict = split(has_curly_bracket.group(1).replace(':', ' ').
                               replace(',', ' '))
                result = result + ' ' + ' '.join(s_dict)
        else:
            result = ' '.join(split(line))

        return result

    def hbnb_parse_args(self, args, command):
        argv = split(args)
        error = None
        if len(argv) == 0 and command != 'all':
            error = "** class name missing **"
        elif len(argv) > 0 and argv[0] not in self.__models_map.keys():
            error = "** class doesn't exist **"
        elif len(argv) == 1 and command not in ['all', 'create', 'count']:
            error = "** instance id missing **"

        return dict({'argv': argv, 'error': error})

    def precmd(self, line):
        return self.hbnb_parse_line(line)

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
        parse_result = self.hbnb_parse_args(args, 'create')
        argv = parse_result['argv']
        error = parse_result['error']
        if error is None:
            new_record = HBNBCommand.__models_map[argv[0]]()
            new_record.save()
            print(new_record.id)
        else:
            print(error)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        parse_result = self.hbnb_parse_args(args, 'show')
        argv = parse_result['argv']
        error = parse_result['error']
        objects = storage.all()
        if error is None:
            if "{}.{}".format(argv[0], argv[1]) not in objects.keys():
                print("** no instance found **")
            else:
                print(objects["{}.{}".format(argv[0], argv[1])])
        else:
            print(error)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        parse_result = self.hbnb_parse_args(args, 'destroy')
        argv = parse_result['argv']
        error = parse_result['error']
        objects = storage.all()
        if error is None:
            if "{}.{}".format(argv[0], argv[1]) not in objects.keys():
                print("** no instance found **")
            else:
                del objects["{}.{}".format(argv[0], argv[1])]
                storage.save()
        else:
            print(error)

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all.
        """
        parse_result = self.hbnb_parse_args(args, 'all')
        argv = parse_result['argv']
        error = parse_result['error']
        if error is None:
            output = []
            records = storage.all().values()
            for rec in records:
                if len(argv) > 0 and argv[0] == rec.__class__.__name__:
                    output.append(rec.__str__())
                elif len(argv) == 0:
                    output.append(rec.__str__())
            print(output)
        else:
            print(error)

    def do_count(self, args):
        """
        Behavior when retrieving the number of record of a given model.
        """
        parse_result = self.hbnb_parse_args(args, 'count')
        argv = parse_result['argv']
        error = parse_result['error']
        if error is None:
            count = 0
            records = storage.all().values()
            for rec in records:
                if argv[0] == rec.__class__.__name__:
                    count += 1
            print(count)
        else:
            print(error)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        parse_result = self.hbnb_parse_args(args, 'update')
        argv = parse_result['argv']
        error = parse_result['error']
        records = storage.all()
        print(args)
        print(argv)

        if error is None:
            if ("{}.{}".format(argv[0], argv[1]) not in records.keys()):
                print("** no instance found **")
                return False
            if len(argv) == 2:
                print("** attribute name missing **")
                return False
            for i in range(2, len(argv), 2):
                to_update = records["{}.{}".format(argv[0], argv[1])]
                if len(argv) > i + 1:
                    if argv[i] in to_update.__class__.__dict__.keys():
                        valtype = type(to_update.__class__.__dict__[argv[i]])
                        to_update.__dict__[argv[i]] = valtype(argv[i + 1])
                    else:
                        to_update.__dict__[argv[i]] = argv[i + 1]
                else:
                    print("** value missing **")
                storage.save()
        else:
            print(error)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
