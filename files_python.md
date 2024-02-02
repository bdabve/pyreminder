<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Opening and reading files with the open() function](#opening-and-reading-files-with-the-open-function)
- [Writing to Files](#writing-to-files)
- [Reading and Writing Binary Data](#reading-and-writing-binary-data)
- [Saving Variables with the shelve Module](#saving-variables-with-the-shelve-module)
- [Pickled Objects](#pickled-objects)
- [DBM Files](#dbm-files)
- [Reading CSV Files](#reading-csv-files)
- [Writing CSV Files](#writing-csv-files)
- [Saving Variables with the pprint.pformat() Function](#saving-variables-with-the-pprintpformat-function)
- [Reading ZIP Files](#reading-zip-files)
- [Extracting from ZIP Files](#extracting-from-zip-files)
- [Creating and Adding to ZIP Files](#creating-and-adding-to-zip-files)

***

## Reading and Writing Files

### Opening and reading files with the open() function

- 
    ```python
    >>> with open('C:\\Users\\your_home_folder\\hello.txt') as hello_file:
    ...     hello_content = hello_file.read()
    >>> hello_content           # 'Hello World!'

    >>> with open('sonnet29.txt') as sonnet_file:
    ...     sonnet_file.readlines()                 # return a list
    [When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my outcast state,\n'
    look upon myself and curse my fate,']

    >>> with open('sonnet29.txt') as sonnet_file:
    ...     for line in sonnet_file:                # note the new line character will be included in the line
    ...         print(line, end='')

# When, in disgrace with fortune and men's eyes,
# And look upon myself and curse my fate,
>>> with open('file.txt', 'r') as f:
...     # Read by a for loop
...     for line in f:
...         print(line)
...         # print(line, end='')
...         # print(line.rstrip())            # to remove blank line(\\n)

...     f_contents = f.read(100)              # Read 100 character

...     # passing read in a loop
...     size_t_read = 10
...     f_contents = f.read(size_t_read)
...     while len(f_contents) > 0:
...         print(f_contents, "*")
...         f_contents = f.read(size_t_read)

>>> lines = [line.rstrip() for line in open('file.txt')]
>>> lines = [line.rstrip().upper() for line in open('file.txt')]
>>> lines = list(map(str.split, open('data.txt')))                    " apply a function"

>>> with open('testFile.txt', 'r') as f:
...     # f.tell() tell where we are in the file
...     size_t_read = 10
...     f_contents = f.read(size_t_read)
...     print("We are in the: ", f.tell(), "th Character.")
...
...     # To manipulate where we are we use seek()
...     size_t_read = 10
...     f_contents = f.read(size_t_read)
...     print(f_contents)
...     f.seek(0)
...     size_t_read = 10
...     f_contents = f.read(size_t_read)
...     print(f_contents)
```
- By default, files are 'read/written' using the system default text encoding, as can be found in sys.getdefaultencoding().
- If you know that the text you are reading or writing is in a different encoding, supply the optional encoding parameter to open

    ```python
    >>> with open('somefile.txt', 'rt', encoding='latin-1') as f:
    ...     # proccess line

- Read with disabled newline translation

    ```python
    >>> with open('somefile.txt', 'rt', newline='') as f:
    ...     # process line
    ```

- Replace bad chars with Unicode U+fffd replacement char

    ```python
    >>> f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
    >>> f.read()                          # 'Spicy Jalape?o!'
    ```

- Ignore bad chars entirely
    ```python
    >>> g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
    >>> g.read()                          # 'Spicy Jalapeo!'
    ```

[*Return to the Top*](#table-of-content)

### Writing to Files

- < w >: if file does not exist Create it; if existe overide its content
- < a >: append

    ```python
    >>> with open('bacon.txt', 'w') as bacon_file:
    ...     bacon_file.write('Hello world!\n')
    13

    >>> with open('bacon.txt', 'a') as bacon_file:
    ...     bacon_file.write('Bacon is not a vegetable.')
    25

    >>> with open('bacon.txt') as bacon_file:
    ...     content = bacon_file.read()

    >>> print(content)
    Hello world!
    Bacon is not a vegetable.
    ```

- Make a copy of file

    ```python
    >>> with open('testFile.txt', 'r') as rf:
    ...     with open('copy_testFile.txt', 'w') as wf:
    ...         wf.write('This is a copy of testFile.txt\\n')
    ...         wf.write('We did it from python\\n')
    ...         for line in rf:
    ...             wf.write(line)
    ```

- Make a copy of an image

    ```python
    >>> with open('eagle.jpg', 'rb') as rf:
    ...     with open('copy_eagle.jpg', 'wb') as wf:
    ...         for line in rf:
    ...             wf.write(line)
    ```

- Write data to a file, but only if it doesn’t already exist on the filesystem
- we use `x` mode to `open()` instead of the usual `w` mode.

    ```python
    >>> with open('somefile', 'wt') as f:
    ...     f.write('Hello\\n')

    >>> with open('somefile', 'xt') as f:
    ...     f.write('Hello\\n')

    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    FileExistsError: [Errno 17] File exists: 'somefile'
    ```

- Write to multiple files at the beggining position

    ```python
    >>> import glob
    >>> files = [f for f in glob.glob('./*.md')]

    >>> for f in files:
    ...     with open(f, 'r+') as input_f:
    ...         content = input_f.read()
    ...         input_f.seek(0, 0)
    ...         input_f.write('<link rel="stylesheet" href="style.css">\n' + content)
    ```

[*Return to the Top*](#table-of-content)

### Reading and Writing Binary Data

- Read the entire file as a single byte string

    ```python
    >>> with open('somefile.bin', 'rb') as f:
    ...    data = f.read()
    ```

- Write binary data to a file

    ```python
    >>> with open('somefile.bin', 'wb') as f:
    ...    f.write(b'Hello World')
    ```

- Decode or encode data

    ```python
    >>> with open('somefile.bin', 'rb') as f:
    ...     data = f.read(16)
    ...     text = data.decode('utf-8')

    >>> with open('somefile.bin', 'wb') as f:
    ...     text = 'Hello World'
    ...     f.write(text.encode('utf-8'))
    ```

### Saving Variables with the shelve Module

- To save variables:

    ```python
    >>> import shelve

    >>> cats = ['Zophie', 'Pooka', 'Simon']
    >>> with shelve.open('mydata') as shelf_file:
    ...     shelf_file['cats'] = cats
    ```

- To open and read variables:

    ```python
    >>> with shelve.open('mydata') as shelf_file:
    ...     print(type(shelf_file))
    ...     print(shelf_file['cats'])
    <class 'shelve.DbfilenameShelf'>
    ['Zophie', 'Pooka', 'Simon']
    ```

- Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf. 
- Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.

    ```python
    >>> with shelve.open('mydata') as shelf_file:
    ...     print(list(shelf_file.keys()))
    ...     print(list(shelf_file.values()))
    ['cats']
    [['Zophie', 'Pooka', 'Simon']]
    ```

| Python code                   | Action    | Description
|-------------------------------|-----------|--------------------------------------------
| file=shelve.open('filename')  | Open      | Create or open an existing shelve’s DBM file
| file['key'] = anyvalue        | Store     |  Create or change the entry for key
| value = file['key']           | Fetch     |  Load the value for the entry key
| count = len(file)             | Size      | Return the number of entries stored
| index = file.keys()           | Index     |  Fetch the stored keys list (an iterable view)
| found = 'key' in file         | Query     |  See if there’s an entry for key
| del file['key']               | Delete    |  Remove the entry for key
| for key in file:              | Iterate   | Iterate over stored keys

- Storing Built-in Object Types in Shelves

    ```python
    >>> import shelve
    >>> object1 = ['The', 'bright', ('side', 'of'), ['life']]
    >>> object2 = {'name': 'Brian', 'age': 33, 'motto': object1}
    >>> with shelve.open('mydbase') as dbase:
    ...     dbase['brian'] = object2
    ...     dbase['knight'] = {'name': 'Knight', 'motto': 'Ni!'}

    >>> dbase = shelve.open('./desktop/shelve_dbase')
    >>> len(dbase)                    # Out: 2
    >>> dbase.keys()                  # Out: KeysView(<shelve.DbfilenameShelf object at 0x7f7d21b51be0>)
    >>> list(dbase.keys())            # Out: ['brian', 'knight']
    >>> dbase['brian']                # Out: {'name': 'Brian', 'age': 33, 'motto': ['The', 'bright', ('side', 'of'), ['life']]}

    >>> for row in dbase:
    ...     print(row, '=>')
    ...     for field in dbase[row]:
    ...         print('   ', field, '=', dbase[row][field])
    # Out:
    brian =>
        name = Brian
        age = 33
        motto = ['The', 'bright', ('side', 'of'), ['life']]
    knight =>
        name = Knight
        motto = Ni!
    ```

- Storing class Instances in Shelves

    ```python
    >>> class Person:
    ...     def __init__(self, name, job, pay=0):
    ...         self.name = name
    ...         self.job = job
    ...         self.pay = pay
    ...     def tax(self):
    ...         return self.pay * 0.25
    ...     def info(self):
    ...         return self.name, self.job, self.pay, self.tax()
    ...     def __repr__(self):
    ...         return '{}({} {})'.format(__class__.__name__, self.name, self.job)
    >>> bob = Person('bob', 'psychologist', 70000)
    >>> emily = Person('emily', 'teacher', 40000)

    # Storing in a shelve file
    >>> with shelve.open('shelve_classes') as dbase:
    ...     for obj in (bob, emily):
    ...         dbase[obj.name] = obj

    # Getting the values
    >>> dbase = shelve.open('shelve_classes')
    >>> dbase['emily']              # Get the __repr__: Person(emily teacher)
    >>> dbase['emily'].tax()        # 10000.0
    >>> dbase['bob'].tax()          # 17500.0
    >>> dbase.close()
    ```

- Changing Classes of Objects Stored in Shelves

    ```python
    # Suppose the Person class from the previous section was changed to
    >>> class Person:
    ...     def __init__(self, name, job, pay=0):
    ...         self.name = name
    ...         self.job = job
    ...         self.pay = pay
    ...     def __getattr__(self, attr):      # On person.attr
    ...         if attr == 'tax':
    ...             return self.pay * 0.30    # computed on access
    ...         else:
    ...             raise AttributeError()    # other unknown names
    ...     def info(self):
    ...         return self.name, self.job, self.pay, self.tax()
    ...     def __repr__(self):
    ...         return '{}({} {})'.format(__class__.__name__, self.name, self.job)

    # Shelve file acquire the new behavior automatically withour resaving our objects.
    >>> dbase = shelve.open('cast')   # reopen shelve
    >>> print(list(dbase.keys()))     # ['bob', 'emily']
    >>> print(dbase['emily'])         # Person(emily teacher)
    >>> print(dbase['bob'].tax)       # no need to call tax()  OUT: 21000.0
    ```
[More on Shelve](file:///home/dabve/python/py_cheatsheet/markdown/14_shelves_example.md)

[*Return to the Top*](#table-of-content)

### Pickled Objects

- Pickling

    ```python
    >>> import pickle
    >>> bob = {'job': 'dev', 'pay': 30000, 'age': 42, 'name': 'Bob Smith'}
    >>> sue = {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
    >>> tom = {'job': None, 'pay': 0, 'age': 50, 'name': 'Tom'}
    >>> db = dict()
    >>> for key, value in ('bob', bob), ('sue', sue), ('tom', tom):
    ...     db[key] = value
    ```

- Storing in a pickle file

    ```python
    >>> with open('people_pickle', 'wb') as dbfile:
    ...     pickle.dump(db, dbfile)
    ```

- Loading pickle files

    ```python
    >>> with open('people_pickle', 'rb') as dbfile:
    ...     db = pickle.load(dbfile)
    >>> type(db)                          # dict
    >>> for key, value in db.items():
    ...     print(key, '=>', value)       # tom =>  {'age': 50, 'job': None, 'pay': 0, 'name': 'Tom'} ...
    ```

- Updating pickle file

    ```python
    >>> db['tom']['job'] = 'hdw'
    >>> db['tom']['pay'] = 30000
    >>> with open('people_pickle', 'wb') as dbfile:
    ...     pickle.dump(db, dbfile)
    ```
- Pickle work with all python datatype

    ```python
    >>> table = {'a': [1, 2, 3], 'b': ['spam', 'eggs'], 'c': {'name':'bob'}}
    >>> mydb = open('dbase', 'wb')        # open for writing
    >>> pickle.dump(table, mydb)

    >>> mydb = open('dbase', 'rb')        # open for reading
    >>> t = pickle.load(mydb)
    >>> print(t)                          # {'a': [1, 2, 3], 'b': ['spam', 'eggs'], 'c': {'name': 'bob'}}
    >>> t['a'][0] = 0                     # change shared object, now call pickle.dump() to update the file
    ```

- Pickle to/from flat file utilities

    ```python
    >>> def save_dbase(filename, object):
    ...     '''Dump Records'''
    ...     with open(filename, 'wb') as f:
    ...         pickle.dump(object, file)         # pickle to binary file

    >>> def load_dbase(filename):
    ...     '''Load object from file'''
    ...     with open(filename, 'rb') as f:
    ...         object = pickle.load(file)        # unpickle from binary file
    ...     return object
    ```

- Pickled with Classes

    ```python
    >>> class Rec:
    ...     def __init__(self, hours):
    ...         self.hours = hours
    ...     def pay(self, rate=50):
    ...         return self.hours * rate

    >>> bob = Rec(40)
    >>> import pickle
    >>> pickle.dump(bob, open('bobrec', 'wb'))

    >>> rec = pickle.load(open('bobrec', 'rb'))
    >>> rec.hours                                     # 40
    >>> rec.pay()                                     # 2000
    ```

[More on Pickles](file:///home/dabve/python/py_cheatsheet/markdown/14_pickle_example.md)

[*Return to the Top*](#table-of-content)

### DBM Files

- DBM files, a standard tool in the Python library for database management, improve on that by providing key-based access to stored text strings.
- They implement a random access, single-key view on stored data.
- For instance, information related to objects can be stored in a DBM file using a unique key per object and later can be fetched back directly with the same key.
- DBM files are implemented by a variety of underlying modules (including one coded in Python), but if you have Python, you have a DBM.
- 'c' argument when calling dbm.open(), force python to create the file if it does not yet exist and to simply open it for reads and writes.

    ```python
    >>> import dbm
    >>> file = dbm.open('movie', 'c')      # Make a DBM file called 'movie', or open file if exist.
    >>> file['Batman'] = 'Pow!'            # Store a string under key 'Batman'
    >>> file.keys()                        # [b'Batman']
    >>> file['Batman']                     # b'Pow!'
    >>> print(type(file['Joker']))         # <class 'bytes'>

    >>> who = ['Robin', 'Cat-woman', 'Joker']
    >>> what = ['Bang!', 'Splat!', 'Wham!']
    >>> for key, value in zip(who, what):
    ...     file[key] = value                         # Adding records to file
    >>> file.keys()                                   # [b'Cat-woman', b'Batman', b'Joker', b'Robin']
    >>> len(file), 'Robin' in file, file['Joker']     # (4, True, b'Wham!')
    >>> file.close()
    ```

- Open an existing file and fetch data.

    ```python
    >>> file = dbm.open('movie', 'c')
    >>> for key in file.keys(): print(key, ':', file[key])                    # this will return keys, values as bytes
    >>> for key in file.keys(): print(key.decode(), ':', file[key].decode())  # decode bytes
    ```

- Make some changes

    ```python
    >>> file['Batman'] = 'Ka-Boom!'                           # change Batman slot
    >>> del file['Robin']                                     # delete the Robin entry
    >>> file.close()
    ```

[*Return to the Top*](#table-of-content)

*** 

### Reading CSV Files

> csv expect delimiter as a coma ','

    ```python
    >>> import csv
    >>> with open('../fileworking/csv_and_json/example_csv.csv') as csv_file:
    ...     csv_reader = csv.reader(csv_file, delimiter=';')
    ...     next(csv_reader)              # skip headers (first line)
    ...     for line in csv_reader:
    ...         print(line)               # print each line
    ...         # print(line[0])          # work with index.
    ```

- Reading as a dict object

    ```python
    >>> with open('../fileworking/csv_and_json/example_csv.csv') as csv_file:
    ...     csv_reader = csv.DictReader(csv_file, delimiter=';')
    ...     for line in csv_reader:
    ...         print(line)
    ...     # print(line['designation'])
    ```

### Writing CSV Files

- Change the delimiter

    ```python
    >>> with open('../fileworking/csv_and_json/example_csv.csv') as csv_file:
    ...    csv_reader = csv.reader(csv_file, delimiter=';')
    ...    # To remove header use
    ...    # next(csv_reader)          # this will skip the first line

    ...     with open('../fileworking/csv_and_json/example_changed_delimiter.csv', 'w') as out_file:
    ...         csv_writer = csv.writer(out_file, delimiter=',')
    ...         for line in csv_reader:
    ...             csv_writer.writerow(line)
    ...     print('Done result in: {}'.format(out_file.name))
    ```
- Delete some columns
- Remove UMesure, Emplacement from our file

    ```python
    >>> with open('../fileworking/csv_and_json/example_csv.csv') as csv_file:
    ...     csv_reader = csv.DictReader(csv_file, delimiter=';')
    ...     with open('../fileworking/csv_and_json/delColumns.csv', 'w') as out_file:
    ...         fields = ['designation', 'code', 'ref', 'qte', 'prixUnitaire']
    ...         csv_writer = csv.DictWriter(out_file, fieldnames=fields, delimiter=',')
    ...         csv_writer.writeheader()   # write headers.

    ...         for line in csv_reader:
    ...         del line['uMesure']
    ...         del line['emplacement']
    ...         csv_writer.writerow(line)
    ...     print('Done Writing to: {}'.format(out_file.name))
    ```

- CSV With `namedtuple()`

    ```python
    >>> with open('project/gs_pyqt/initial_etats.csv') as csv_f:
    ...     csv_reader = csv.reader(csv_f, delimiter=';')
    ...     headings = next(csv_reader)
    ...     Row = namedtuple('Row', headings)
    ...     rows = [Row(*line) for line in csv_reader]

    >>> for r in rows:
    ...    if r.code == 'MOS-069':
    ...         print(r)
    ```

- Convert data

    ```python
    >>> for r in rows[:1]:
    ...     print(type(r.qte))            # <class 'str'>

    >>> from decimal import Decimal
    >>> col_types = [str, str, str, str, str, int, Decimal]
    >>> with open('./project/gs_pyqt/initial_etats.csv') as f:
    ...     reader = csv.reader(f, delimiter=";")
    ...     headers = next(reader)
    ...     Row = namedtuple('Row', headers)
    ...     rows = []
    ...     for row in reader:
    ...         row = tuple(convert(value) for convert, value in zip(col_types, row))
    ...         rows.append(Row(*row))
    
    >>> for r in rows[:5]:
    ...     print(type(r.qte))            # < class 'str' >
    ...     print(type(r.prixUnitaire))   # <class 'decimal.Decimal'>
    ```

- Conversion with the Dict Object

    ```python
    >>> field_types = [('designation', str), ('code', str), ('ref', str), ('um', str), ('emp', str), ('qte', int), ('prixUnitaire', Decimal)]
    >>> with open('./project/gs_pyqt/initial_etats.csv') as f:
    ...     dict_reader = csv.DictReader(f, delimiter=';')
    ...     for row in dict_reader:
    ...         row.update((key, conversion(row[key])) for key, conversion in field_types)
    ...         print(type(row['prixUnitaire']))
    ```

[*Return to the Top*](#table-of-content)

### Saving Variables with the pprint.pformat() Function

```python
>>> import pprint

>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"

>>> with open('myCats.py', 'w') as file_obj:
...     file_obj.write('cats = {}\n'.format(pprint.pformat(cats)))
83
```

[*Return to the Top*](#table-of-content)

### Reading ZIP Files

- `namelist()` : returns a list of strings for all the files and folders contained in the ZIP file.

    ```python
    >>> import zipfile, os

    >>> os.chdir('C:\\')    # move to the folder with example.zip
    >>> with zipfile.ZipFile('example.zip') as example_zip:
    ...     print(example_zip.namelist())
    ...     spam_info = example_zip.getinfo('spam.txt')
    ...     print(spam_info.file_size)
    ...     print(spam_info.compress_size)
    ...     print('Compressed file is %sx smaller!' % (round(spam_info.file_size / spam_info.compress_size, 2)))

    ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
    13908
    3828
    'Compressed file is 3.63x smaller!'
    ```

[*Return to the Top*](#table-of-content)

### Extracting from ZIP Files

- The `extractall()` method for ZipFile objects extracts all the files and folders from a ZIP file into the current working dir.
- You can pass a folder name to extractall() to have it extract the files into a folder.
- If the folder passed to the extractall() method does not exist, it will be created.

    ```python
    >>> with zipfile.ZipFile('exampla.zip') as zip_file:
    ...     zip_file.extractall('folder_out')                       # extract all zip in folder_out
    ...     # Extract one file
    ...     zip_file.extract('spam.txt')                              # Out: 'C:\\spam.txt'
    ...     # Extracting into a folder, if folder doesn't exist will create it.
    ...     zip_file.extract('spam.txt', 'C:\\some\\new\\folders')    # Out: 'C:\\some\\new\\folders\\spam.txt'
    ```

- The `extract()` method for ZipFile objects will extract a single file from the ZIP file.

    ```python
    >>> with zipfile.ZipFile('example.zip') as example_zip:
    ...     print(example_zip.extract('spam.txt'))
    ...     print(example_zip.extract('spam.txt', 'C:\\some\\new\\folders'))
    'C:\\spam.txt'
    'C:\\some\\new\\folders\\spam.txt'
    ```

[*Return to the Top*](#table-of-content)

### Creating and Adding to ZIP Files

- To create your own compressed ZIP files, you must open the ZipFile object in write mode.
- The < write() > method's first argument is a string of the filename to add.
- The second argument is the compression type parameter, which tells the computer what algorithm it should use.
- You can always just set this value to < zipfile.ZIP_DEFLATED >.
- This specifies the deflate compression algorithm, which works well on all types of data.

    > NB: < Write > mode will erase all existing contents of a ZIP file. 
If you want to simply add files to an existing ZIP file, pass 'a' as the second argument to zipfile.ZipFile().

    ```python
    >>> import zipfile

    >>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
    ...     new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    ```

- This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.

[*Return to the Top*](#table-of-content)
