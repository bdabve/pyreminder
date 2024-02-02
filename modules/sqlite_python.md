<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="style.css">

## Table of Content

- [Connecting to a database](#connecting-to-a-database)
- [Droping table](#droping-table)
- [Creating table people](#creating-table-people)
- [INSERT Statement](#insert-statement)
- [SELECT Statement](#select-statement)
- [UPDATE and DELETE statement](#update-and-delete-statement)
- [Using Table Descriptions](#using-table-descriptions)
- [Record Dictionaries Construction](#record-dictionaries-construction)
- [Work with Rows as a Dict](#work-with-rows-as-a-dict)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## sqlite3

### Connecting to database

```python
import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('dbase.sqlite')     # connect to database if file does not exists will create it
except Error as err:
    print(f'Err: {err}')
else:
    curs = conn.cursor()
```

[*Return to the Top*](#table-of-content)

### Droping table

```python
try:
    curs.execute('DROP TABLE people')
except Error as err:
    print(f'Err: {err}')
```

[*Return to the Top*](#table-of-content)

### Creating table people

```python
tbl_query = """create table people(
            id int not null primary key,
            name char(30),
            job char(10),
            pay int(4)
            )"""
print('[+] Creating table: people')
try:
    curs.execute(tbl_query)
except Error as err:
    print(f'Err: {err}')
```

[*Return to the Top*](#table-of-content)

### INSERT Statement

- Inserting some values

    ```python
    try:
        curs.execute('INSERT INTO people VALUES(?, ?, ?, ?)', (1, 'Bob', 'dev', '5000'))
    except Error as err:
        print(f'Err: {err}')
    else:
        print('Affected rows: {}'.format(curs.rowcount))
        print('Param style: {}'.format(sqlite3.paramstyle))
    ```

- Insert multiple rows with a single statement

    ```python
    try:
        curs.executemany("INSERT INTO people VALUES(?, ?, ?, ?)", [(2, 'Sue', 'mus', '70000'), (3, 'Ann', 'mus', '60000')])
    except Error as err:
        print(f'Err: {err}')
    else:
        print('Affected rows: {}'.format(curs.rowcount))
    ```

- Inserting one row at a time with python loop:

    ```python
    rows = [[4, 'Tom', 'mgr', 100000],
            [5, 'Kim', 'adm', 30000],
            [6, 'Pat', 'dev', 90000]]
    affected_row = 0

    for row in rows:
        try:
            curs.execute('INSERT INTO people VALUES(?, ?, ?, ?)', row)
        except Error as err:
            print(f'Err: {err}')
        else:
            affected_row += int(curs.rowcount)
            conn.commit()         # We have to commit changes.

    print('Affected rows: {}'.format(affected_row))
    ```

- Inserting one row like in PHP:

    ```python
    try:
        curs.execute("INSERT INTO people VALUES (:id, :name, :job, :pay)", {'id': 7, 'name': 'Dabve', 'job': 'dev', 'pay': 35000})
    except Error as err:
        print(f'Err: {err}')
    else:
        conn.commit()               # Commit changes
        print('Affected rows: {}'.format(curs.rowcount))
    ```

[*Return to the Top*](#table-of-content)

### SELECT Statement

```python
try:
    curs.execute('SELECT * FROM people')
except Error as err:
    print(f'Err: {err}')
else:
    for row in curs.fetchall():
        print('{}'.format(row))
```

- if we now column count we can do

    ```python
    try:
        curs.execute('SELECT * FROM people')
    except Error as err:
        print(f'Err: {err}')
    else:
        for (pid, name, job, pay) in curs.fetchall():
            print('{} {} {} {}'.format(pid, name, job, pay))
    ```

- use a Python list comprehension to pick out the fields we want

    ```python
    try:
        curs.execute('SELECT * FROM people')
    except Error as err:
        print(f'Err: {err}')
    else:
        names = [rec[1] for rec in curs.fetchall()]
        for name in names:
            print(name)
    ```

- selecting data like in PHP:

    ```python
    try:
        curs.execute("SELECT * FROM people WHERE pay=:pay", {'pay': 34000})
    except Error as err:
        print(f'Err: {err}')
    else:
        for row in curs.fetchall():
            print(row)
    ```

- The fetchone call returns the next result row or a None(false) value at the end of the table

    ```python
    try:
        curs.execute('SELECT * FROM people')
    except Error as err:
        print(f'Err: {err}')
    else:
        while True:
            row = curs.fetchone()
            if not row:
                break
            print('\t', row)
    ```

- The fetchmany call returns a sequence of rows from the result, but not the entire table.
- You can specify how many rows to grab each time.

    ```python
    try:
        curs.execute('SELECT * FROM people')
    except Error as err:
        print(f'Err: {err}')
    else:
        while True:
            row = curs.fetchmany()      # size=N optional argument
            if not row:
                break
            print('\t', row)
    ```

[*Return to the Top*](#table-of-content)

### UPDATE and DELETE statement

```python
print('UPDATING Somme Rows')
curs.execute('UPDATE people SET pay=? WHERE pay<=?', [65000, 60000])
print('Affected rows: {}'.format(affected_row))

print('DELETING Somme Rows')
curs.execute('DELETE FROM people WHERE name = ?', ['Bob'])
curs.execute('DELETE FROM people WHERE pay >= ?', (90000,))
```

- Finally, remember to commit you changes to the database before exiting Python, assuming you wish to keep them.

    ```python
    conn.commit()
    ```

[*Return to the Top*](#table-of-content)

### Using Table Descriptions

- The cursor's description attribute gives the names and type of the columns in the result table.
- The sqlite3 module implements only the name component:`(name, type_code, display_size, internal_size, precision, scale, null_ok)`

    ```python
    try:
        curs.execute('SELECT * FROM people')
    except Error as err:
        print(f'Err: {err}')
    else:
        colnames = [desc[0] for desc in curs.description]
        print(colnames)
        for row in curs.fetchall():
            for name, value in zip(colnames, row):
                print('{} \t=> {}'.format(name, value))
    ```

[*Return to the Top*](#table-of-content)

### Record Dictionaries Construction

```python
try:
    curs.execute('SELECT * FROM people')
except Error as err:
    print(f'Err: {err}')
else:
    colnames = [desc[0] for desc in curs.description]
    rowdicts = list() 
    for row in curs.fetchall():
        # rowdicts.append(dict(zip(colnames, row)))        # The same resutl in one line
        newdict = {}
        for name, val in zip(colnames, row):
            newdict[name] = val
        rowdicts.append(newdict)
```

- A list comprehenstion will do the job of collecting the dict into a list

    ```python
    try:
        curs.execute('SELECT * FROM people')
    except Error as err:
        print(f'Err: {err}')
    else:
        colnames = [desc[0] for desc in curs.description]
        rowdicts = [dict(zip(colnames, row)) for row in curs.fetchall()]
        print(rowdicts)
    ```

### Work with Rows as a Dict

```python
try:
    conn = sqlite3.connect('dbase.sqlite')
except Error as err:
    print(err)
else:
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()
    curs.execute('select * from tablename')
    row = curs.fetchone()
    print(row.keys())           # column names
    print(row['designation'])   # we can navigate with key name
finally:
    if conn:
        conn.close()            # Closing connection to the database.
```

[*Return to the Top*](#table-of-content)
