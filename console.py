#!/usr/bin/python3
"""Console"""
import cmd
from models.base_model import BaseModel
from models import storage


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
            print ("** class name missing **")
        elif arg != "BaseModel":
            print ("** class doesn't exist **")
        else:
            objarg = BaseModel()
            storage.new(objarg)
            storage.save
            print (BaseModel.id)
    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        if len(arg) < 2:
            print ("** class name missing **")
        elif len(arg) < 3:
            print ("** instance id missing **")
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if len(arg) < 2:
            print ("** class name missing **")
        elif len(arg) < 3:
            print ("** instance id missing **")
    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if len(arg) < 2:
            print ("** class name missing **")
        elif len(arg) < 3:
            print ("** instance id missing **")
        elif len(arg) < 4:
            print ("")
    def emptyline(self):
        return None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
