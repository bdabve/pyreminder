<link rel="stylesheet" href="style.css">
- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

# <center>using pickle</center>

- The pickle module translates an in-memory Python object into a serialized byte stream—a string of bytes that can be written to any file-like object.
- The pickle module also knows how to reconstruct the original object in memory, given the serialized byte stream: we get back the exact same object. In a sense, the pickle module replaces proprietary data formats its serialized format is general and efficient enough for any program.
- With pickle, there is no need to manually translate objects to data when storing them persistently, and no need to manually parse a complex format to get them back.
- Pickling is similar in spirit to XML representations, but it’s both more Python-specific, and much simpler to code.

```python

import pickle

# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

def db_pickle(out_file):
    """
    Store dicts values from imported file initdata.py with pickle module to out_file
    """
    with open(out_file, 'wb') as db_file:     # use binary mode
        pickle.dump(db, db_file)              # data is bytes, not str
        print('[+] Done storing data in binary format in : {}'.format(out_file))


def dump_db_file(input_file):
    """
    dump data from pickled file and translatit back to python dicts
    """
    with open(input_file, 'rb') as db_file:
        unpickled = pickle.load(db_file)

    print('\n[+] Loading file {}'.format(input_file))
    for key in unpickled:
        print('{} => {}'.format(key, unpickled[key]))
    print('End of file.')


def update_db_file(input_file, out_file):
    """
    open a pickled file
    modify it
    write changes to out file.
    """
    with open(input_file, 'rb') as db_file:
        unpickled = pickle.load(db_file)
    # updating records
    unpickled['sue']['pay'] *= 1.10
    unpickled['tom']['name'] = 'Tom Tom'

    with open(out_file, 'wb') as db_file:
        pickle.dump(unpickled, db_file)
    print('[+] Done writing changes to: {}'.format(out_file))


db_pickle('people_pickle')
update_db_file('people_pickle', 'people_pickle')
dump_db_file('people_pickle')
```
