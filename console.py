#!/usr/bin/python3
"""Console"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import storage


Dict = {"City": City, "User": User, "Place": Place, "Review": Review,
        "Amenity": Amenity, "State": State, "BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """console for Airbnb clone"""
    prompt = '(hbnb)'
    intro = None
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id."""
        if len(arg) < 1:
            print("** class name missing **")
        elif arg in Dict:
            newid = Dict[arg]()
            newid.save()
            print(newid.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        tf = "false"
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in Dict:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                for i in storage.all():
                    arggs = str(storage.all()[i]).split()
                    cid = arggs[1][slice(1, -1)]
                    if cid == args[1]:
                        print("{}".format(storage.all()[i]))
                        tf = "true"
                        storage.save()
                        break
                if tf == "false":
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        tf = "false"
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in Dict:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                for i in storage.all():
                    arggs = str(storage.all()[i]).split()
                    cid = arggs[1][slice(1, -1)]
                    if cid == args[1]:
                        storage.all().pop(key, None)
                        tf = "true"
                        storage.save()
                        break
                if tf == "false":
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        args = arg.split()
        new_list = []
        if len(args) > 0:
            if args[0] in Dict:
                for i in storage.all():
                    args = str(storage.all()[i]).split(" ")
                    if args[0] == "[" + arg + "]":
                        new_list.append(str(storage.all()[i]))
                print(new_list)
            else:
                print("** class doesn't exist **")
        else:
            for i in storage.all():
                new_list.append(str(storage.all()[i]))
            print(new_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        tf = "false"
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in Dict:
            if len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if args[3][0] == "\"":
                    value = args[3][slice(1, -1)]
                else:
                    value = args[3]
                for i in storage.all():
                    arggs = str(storage.all()[i]).split()
                    cid = arggs[1][slice(1, -1)]
                    if cid == args[1]:
                        setattr(storage.all()[i], args[2], str(value))
                        storage.save()
                        tf = "true"
                        break
                if tf == "false":
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Checks what is input for command"""
        args = line.split(".")
        newline = ""
        if len(args) > 1:
            command = args[1].split()
            if command[0] == "all()":
                cmd = command[0][slice(0, 3)]
                testline = ("{} {}".format(cmd, args[0]))
                self.onecmd(testline)
            elif "count()" in command[0]:
                count = 0
                if args[0] in Dict:
                    for i in storage.all():
                        arggs = str(storage.all()[i]).split(" ")
                        if arggs[0] == "[" + args[0] + "]":
                            count += 1
                    print(count)
            elif "show" in command[0]:
                cid = command[0][slice(5, -1)]
                cmd = command[0][slice(0, 4)]
                testline = ("{} {} {}".format(cmd, args[0], cid))
                self.onecmd(testline)
            elif "destroy" in command[0]:
                cid = command[0][slice(9, -2)]
                cmd = command[0][slice(0, 7)]
                testline = ("{} {} {}".format(cmd, args[0], cid))
                self.onecmd(testline)
            elif "update" in command[0]:
                cmd = command[0][slice(0, 6)]
                if len(args) > 0:
                    newargs = args[1].split(" ")
                cid = newargs[0][slice(7, -1)]
                if len(newargs) >= 1:
                    name = newargs[1][slice(0, -1)]
                if len(newargs) >= 2:
                    value = newargs[2][slice(0, -1)]
                testline = ("{} {} {} {} {}".format(cmd, args[0], cid, name,
                                                    value))
                self.onecmd(testline)

    def emptyline(self):
        return None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
