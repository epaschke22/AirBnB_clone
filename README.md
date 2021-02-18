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

| Commands | Descriptions |
| ----------- | ----------- |
| create {ClassName} | *Returns created objects id* |
| show {ClassName} {id} | *Shows what is in the object you created*|
| all {ClassName} | *Displays all objects with given class name (Class name is not required)* |
| destroy {ClassName} {id} | *Destroys an object with the given ClassName and id* |
| update {ClassName} {id} {attribute_name} {attribute_value} | *Updates object with given ClassName and id with the given attribute_name and attribute_value* |

## Examples
```
(hbnb)create BaseModel
bd2003b0-6a17-4551-a588-bc9fc3e0df4b
(hbnb)show BaseModel bd2003b0-6a17-4551-a588-bc9fc3e0df4b
[BaseModel] (bd2003b0-6a17-4551-a588-bc9fc3e0df4b) {'updated_at': datetime.datetime(2021, 2, 18, 4, 24, 19, 704992), 'created_at': datetime.datetime(2021, 2, 18, 4, 24, 19, 704977), 'id': 'bd2003b0-6a17-4551-a588-bc9fc3e0df4b'}
(hbnb)update BaseModel bd2003b0-6a17-4551-a588-bc9fc3e0df4b first_name Bob
(hbnb)show BaseModel bd2003b0-6a17-4551-a588-bc9fc3e0df4b
[BaseModel] (bd2003b0-6a17-4551-a588-bc9fc3e0df4b) {'updated_at': datetime.datetime(2021, 2, 18, 4, 24, 19, 704992), 'created_at': datetime.datetime(2021, 2, 18, 4, 24, 19, 704977), 'first_name': 'Bob', 'id': 'bd2003b0-6a17-4551-a588-bc9fc3e0df4b'}
(hbnb)destroy BaseModel bd2003b0-6a17-4551-a588-bc9fc3e0df4b
(hbnb)show BaseModel bd2003b0-6a17-4551-a588-bc9fc3e0df4b
** no instance found **
```

### Extra
**Command Aliases**
| Commands | Alias |
| ----------- | ----------- |
| show | {ClassName}.show({id}) |
| all | {ClassName}.all() |
| destroy | {ClassName}.destroy({id}) |
| update | {ClassName}.update({id}, {attribute_name}, {attribute_value})|
**Other Commands**
| Commands | Descriptions |
| ----------- | ----------- |
| {ClassName}.count() | counts number of objects with given class name|