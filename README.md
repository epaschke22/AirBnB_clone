# AirBnB_clone

The AirBnB project allows us to create and manipulate a dictonary of objects
that we are able to push and update to a json file. Some of the data in this
file includes date/time created and updated, its very own uuid, and much more

The command interpreter includes the commands create, show, all,
destroy, update, and count. All these command manipulate a .json file through a
dictionary of objects.

**How to use the command interpreter**
you start with ./console to initiate the command interpreter then from here you
are able to use the following commands to create and manipulate dictionaries.

**Commands**
- create {ClassName}
*Returns created objects id*
- show {ClassName} {id} or {ClassName}.show({id})
*Shows what is in the class you created*
- all {ClassName} or {ClassName}.all()
*The class name is optional and will show every object with the ClassName*
- destroy {ClassName} {id} or {ClassName}.destroy({id})
*Destroys an object with the given ClassName and id*
- update {ClassName} {id} {key_name} {key_value} or {ClassName}.update({id}, {key_name}, {key_value})
*Updated given ClassName and id with the given key_name and key_value*