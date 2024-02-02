<link rel="stylesheet" href="style.css">
## Table of Content

- [MySQL connection arguments list](#mysql-connection-arguments-list)
- [Listing all database in a server](#listing-all-database-in-a-server)
- [Listing Tables and Checking if Table Exists](#listing-tables-and-checking-if-table-exists)
- [Accessing Table Columns definitions](#accessing-table-columns-definitions)
- [Create and Populate Table](#create-and-populate-table)
- [Selecting Data](#selecting-data)
- [Fetch Methods](#fetch-methods)
- [Transaction Support](#transaction-support)
- [Querying Data](#querying-data)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## MySQL Connector

### Install on ubuntu

```bash
$ pip3 install mysql-connector-python
```

### MySQL connection arguments list

| Options             | Meaning                                                                           | Default value
|---------------------|-----------------------------------------------------------------------------------|--------------------
| `port`              | The TCP/IP port of the MySQL server. This value must be an integer.               | 3306
| `use_unicode`       | Whether to us Unicode.                                                            | True
| `charset`           | MySQL character set to use.                                                       | 'utf8'
| `auto-commit`       | Whether to auto-commit transactions.                                              | 'False'
| `get_warnings`      | To fetch warning.                                                                 | False'
| `raise_on_warnings` | Whether to raise an exception on warnings.                                        | False
| `buffered`          | Whether cursor object fetch the results immediately after executing queryes.      | False
| `raw`               | Whether MySQL results are returned as is, rather than converted to python types.  | False
| `force_ipv6`        | uses IPv6 when an address resolves to both IPv4 and IPv6.                         | False

> connection_timeout(connect_timeout*): Timeout for the TCP and unix socket connections.

- Example

    ```python
    >>> conn_params = {'database': 'cookbook', 'host': 'localhost', 'user': 'baduser', 'password': 'badpass'}
    >>> conn_params = {'database': 'cookbook',
                        'unix_socket': '/var/tmp/mysql.sock',
                        'user': 'baduser',
                        'password': 'badpass',
                        'port':3307}
    >>> try:
    ...     conn = mysql.connector.connect(**conn_params)
    ...     print('Connected')
    ... except mysql.connector.Error as e:
    ...     print('Cannot connect to server')
    ...     print('Error code: %s' % e.errno)
    ...     print('Error message: %s' % e.msg)
    ...     print('Error SQLSTATE: %s' % e.sqlstate)
    ```

- Use the dictionary to keep MySQL connection

    ```python
    >>> import mysql.connector
    >>> from mysql.connector import Error
    >>> from mysql.connector import errorcode

    >>> connection_config = { 'user': 'username',
                              'passowr': 'passwd',
                              'host': '127.0.0.1',
                              'database': 'db-name',
                              'raise_on_warnings': True,
                              'use_pure': False,
                              'autocommit': True,
                              'pool_size': 5 }
    >>> try:
    ...     conn = mysql.connector.connect(**connection_config)
    ...     if connection.is_connected():
    ...         db_info = connection.get_server_info()
    ...         print("Succesfully connected, MySQL server version on: ", db_info)
    >>> except Error as err:
    ...     print('Error: ', err)
    >>> finally:
    ...     if connection.is_connected():
    ...         connection.close()
    ```

- OR

    ```python
    >>> try:
    ...     con =  mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employees')

    ...     # The cursor is used to traverse the records from the result set.
    ...     cur = con.cursor()
    ...     cur = con.cursor(dictionary=True)             # dictionary cursor
    ... except mysql.connector.Error as e:
    ...     print('Error {}: {}'.format(e.args[0], e.args[1]))
    ... finally:
    ...     if connection.is_connected():
    ...         connection.close()
    ```


[*Return to the Top*](#table-of-content)

### Listing all database in a server

```python
>>> cur.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA")
>>> rows = cur.fetchall()
>>> for r in rows:
...     print(r)
```


[*Return to the Top*](#table-of-content)

### Listing Tables and Checking if Table Exists

- Listing all Tables in DB

  ```python
  cur.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_name'")
  ```

- Checking if table exists

  ```python
  cur.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_name' AND TABLE_NAME = 'table_name'")
  cur.execute("SHOW CREATE TABLE table_name")
  ```

[*Return to the Top*](#table-of-content)

### Accessing Table Columns definitions

- To retrieve information about all columns, omit the COLUMN_NAME condition

    ```python
    cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'db_name' AND TABLE_NAME = 'table_name'
                 AND COLUMN_NAME = 'column_name'")
    cur.execute("SHOW COLUMNS FROM table_name LIKE 'column_name'")
    ```

- To retrieve only certain types

    ```python
    cur.execute("SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'db_name'
                 AND TABLE_NAME = 'table_name' AND COLUMN_NAME = 'column_name'")
    ```

[*Return to the Top*](#table-of-content)

### Create and populate table

```python
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   conn = mysql.connector.connect(host='localhost', database='python_db', user='pynative', password='pynative@#29')
   query = 'INSERT INTO `python_users`(`id`, `name`, `birth_date`, `age`) VALUES (1,'Scott','2018-04-11', 26)'
   cur = conn.cursor()
   result = cur.execute(query)      # if we want to verify
   conn.commit()
   print ("Record inserted successfully into python_users table")
except Error as error :
    conn.rollback()             # rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))
finally:
    # closing database connection.
    if conn.is_connected():
        cur.close()
        conn.close()
        print("MySQL connection is closed")
```

- Insert new employee

    ```python
    add_employee = "INSERT INTO employees(first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)"
    data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
    cursor.execute(add_employee, data_employee)
    emp_no = cursor.lastrowid
    ```

- Insert salary information

    ```python
    add_salary = ("INSERT INTO salaries(emp_no, salary, from_date, to_date)
                   VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
    data_salary = {'emp_no': emp_no, 'salary': 50000, 'from_date': tomorrow, 'to_date': date(9999, 1, 1)}
    cursor.execute(add_salary, data_salary)

    cnx.commit()            # Make sure data is committed to the database
    cnx.rollback()          # Or rollback
    cursor.close()
    cnx.close()
    ```

- Using cursor's executemany()

    ```python
    import mysql.connector
    from mysql.connector import Error
    from mysql.connector import errorcode
    try:
       conn = mysql.connector.connect(host='localhost', database='python_db', user='pynative', password='pynative@#29'
                                            use_pure=True)      # use_pure is obligatory for prepared stmt
       records = [ (2,'Jon','2018-01-11', 26) , (3,'Jane','2017-12-11', 27), (4,'Bill','2018-03-23', 26) ]
       query = 'INSERT INTO python_users (id, name, birth_date, age) VALUES (%s,%s,%s,%s)'

       cur = connection.cursor(prepared=True)        # Prepared stmt
       # used executemany to insert 3 rows
       result  = cur.executemany(sql_insert_query, records_to_insert)        # executemany stmt with one cursor
       conn.commit()
       print (cur.rowcount, "Record inserted successfully into python_users table")      # rowcount
    except Error as error :
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if(conn.is_connected()):
            cur.close()
            conn.close()
            print("connection is closed")
    ```

[*Return to the Top*](#table-of-content)

### Selecting data

```python
import mysql.connector
from mysql.connector import Error
try:
   conn = mysql.connector.connect(host='localhost', database='python_db', user='pynative', password='pynative@#29')
   query = "SELECT * FROM python_developers"
   cur = conn.cursor()
   cur.execute(query)
   rows = cur.fetchall()
   print("Total number of rows in python_developers is - ", cur.rowcount)
   for row in rows:
       print("Id = ", row[0], ' Name: ', row[1], ' JoiningDate: ', row[2], ' Salary: ', row[3], '\n')
   cur.close()       # Closing cursor
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
```

- With variables

    ```python
    conn = mysql.connector.connect(host='localhost', database='python_db', user='pynative', password='pynative@#29'
                                            use_pure=True)      # use_pure is obligatory for prepared stmt
    cur = conn.cursor(prepared=True)
    query = 'SELECT * FROM python_developers WHERE id = %s'
    cursor.execute(query, (1, ))
    rows = cursor.fetchall()
    ```

[*Return to the Top*](#table-of-content)

### Fetch methods

- fetchone methode print one row

    ```python
    cursor.execute("SELECT * FROM FromPython")
    output = cursor.fetchone()
    print(output)

    # with a for loop
    for i in range(cur.rowcount):
        row = cur.fetchone()
        print(row[0], row[1])
    ```

- fetchmany specified rows in size

    ```python
    cursor.execute("SELECT * FROM movies")
    output2 = cursor.fetchmany(2)
    print(output2)
    ```

- Print column headers.

    ```python
    cur = con.cursor()
    cur.execut("SELECT * FROM FromPython")
    rows = cur.fetchall()
    desc = cur.description
    print("{} {:>10}".format(desc[0][0], desc[1][0]))
    for row in rows:
        print("{}".format(row))
    ```

- Prepared Statement

    ```python
    cur = con.cursor()
    cur.execute("UPDATE FromPython SET Name = %s WHERE id = %s", ("Guy de Maupasant", "4"))
    print("Number of updated rows: {}".format(cur.rowcount))

    add_salary = ("INSERT INTO salaries(emp_no, salary, from_date, to_date)
                   VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s")

    # Insert salary information
    data_salary = {'emp_no': emp_no, 'salary': 50000, 'from_date': tomorrow, 'to_date': date(9999, 1, 1)}
    cursor.execute(add_salary, data_salary)
    ```

[*Return to the Top*](#table-of-content)

### Transaction support

- The python interface silently starts a transaction when the cursor is created.
- In python DB API, we do not call the BEGIN statement to start transaction.
- A transaction is started when the cursor is created.
- The commit() method commits the updates made using the cursor.
- The rollback() method discards them

    ```python
    try:
        cur.execute("INSERT INTO FromPython(Name) VALUES('Jack London')")
        con.commit()     # save changes
    except mdb.MySQLErro as e:
        if con:
            con.rollback()
        print("Error: {0[0]}: {0[1]}".format(e.args))
    finally:
        if con:
            con.close()
    ```

[*Return to the Top*](#table-of-content)

### Querying Data

```python
query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
    print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))
```

[*Return to the Top*](#table-of-content)
