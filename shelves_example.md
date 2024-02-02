<link rel="stylesheet" href="style.css">
- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

# <center>Working with shelve</center>

- The shelve interface is just as simple it is identical to dictionaries, with extra open and close calls.
- A shelve really does appear to be a persistent dictionary of persistent objects; Python does all the work of mapping its content to and from a file.

```python
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

import shelve

with shelve.opent('people-shelve') as db
    for (key, value) in (('bob', bob), ('sue', sue)):
        print('Adding: {} => {} to people-shelve'.format(key, value))
        db[key] = value

def dump_shelve_db(input_file):
    db = shelve.open(input_file)
    sue = db['sue']             # fetch sue
    sue['pay'] *= 1.50
    db['sue'] = sue             # update sue
    print(db['sue'])
    db['tom'] = tom             # add tom to db
    print(db['tom'])
    db.close()

dump_shelve_db('people-shelve')
```

- This script creates one or more files in the current directory with the name peopleshelve as a prefix (in Python 3.1 on Windows, people-shelve.bak, people-shelve.dat, and people-shelve.dir).
- You shouldn’t delete these files (they are your database!), and you should be sure to use the same base name in other scripts that access the shelve.


## Working with classes

```python

class Person:

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        """self argument to access or update the instance(record) being processed"""
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<{} => {} {} {}>'.format(self.__class__.__name__, self.name, self.job, self.pay)


bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)             # Job assigned automatically

db = shelve.open('shelve_classes')
with shelve.open('shelve_classes') as db:
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    print('Done adding all records.')


def dump_shelve_classes(input_file):
    """
    When instances are shelved or pickled, the underlying pickling system records both instance attributes and enough informations
    to locate thier classes automatically when they are later fetched. we don't need to reimport the class
    """
    with shelve.open(input_file):
        for key in db:
            print('{} => name: {}, pay: {}'.format(key, db[key].name, db[key].pay))
        bob = db['bob']
        print('[+] bob last name: {}'.format(bob.lastName()))
        print('[+] tom last name: {}'.format(db['tom'].lastName()))


def update_shelve_classes(input_file):
    with shelve.open(input_file) as f:
        sue = f['sue']
        sue.giveRaise(.25)
        f['sue'] = sue
        tom = f['tom']
        tom.giveRaise(.20)
        f['tom'] = tom

update_shelve_classes('shelve_classes')
```

## Another Example:

```python
fieldnames = ('name', 'age', 'job', 'pay')

with shelve.open('./shelve_classes') as db:
    while True:
        key = input('\nKey? => ')
        if not key: break
        if key in db:
            record = db[key]                        # update existing record
        else:                                       # or make/store new rec
            record = Person(name='?', age='?')      # eval: quote strings
        for field in fieldnames:
            # getattr : fetch an object's attribute when given its name string
            currval = getattr(record, field)
            newtext = input('\t[{}]={}\n\t\tnew?=>'.format(field, currval))
            if newtext:
                setattr(record, field, eval(newtext))
                # setattr: assign an attribute given its name string
                # eval   : allows any Python object type, but it means you must quote string inputs explicitly
        db[key] = record
```
