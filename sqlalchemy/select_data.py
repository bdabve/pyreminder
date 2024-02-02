#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : select_data.py
#      CREATED : 11-November-2019
#       AUTHOR : daBve, dabve@outlook.fr
#
#         DESC : Querying Data
#        USAGE : ./select_data.py
# ====================================================================================================

from sqlalchemy import create_engine
from sqlalchemy.sql import select
from create_tables import cookies, login

# engine = create_engine('postgresql+psycopg2://dabve:sqlUbuntu@localhost:5432/dabve', pool_recycle=3600)
engine = create_engine('sqlite:///sql_alchemy.sqlite')
conn = login(engine)


# -----------------------------------------------------
# Get All Rows
# -------------
query = select([cookies])       # query = cookies.select() to get all values from a table.
# print(str(query))             # print the query
rows = conn.execute(query)      # ResultProxy
all_result = rows.fetchall()

# first_row = results[0]                    # get the first row of ResultProxy
# print(first_row[1])                       # Access column by index            : 'chocolate chip'
# print(first_row.cookie_name)              # Access column by name             : 'chocolate chip'
# print(first_row[cookies.c.cookie_name])   # Access column by Column Object    : 'chocolate chip'

print('---- All Records ----')
for row in all_result:
    # print(row)                            # as tuple
    print(row.cookie_name)                  # by name like a namedtuple object
    # print(row[cookies.c.cookie_name])     # access column by Column object.
    print(row.cookie_name)                  # by name like a namedtuple object

# first(): Returns the first record if there is one, and closes the connection.
print()
print('---- first() ----')
rows = conn.execute(query)
first_row = rows.first()      # Another syntax: result = conn.execute(query).first()
print(first_row)

# ==| fetch column with result.keys() |== #
# for key in result.keys():
#   print('{:>20}: {}'.format(key, result[key]))

# fetchone(): Return one row, and leaves the cursor open for you to make additional fetch calls.
print()
print('---- fetchone() ----')
rows = conn.execute(query)
one_record = rows.fetchone()          # get the first row
print(one_record)

# scalar(): Return a single value if a query results in a single record with one column.
print()
print('---- scalar() ----')
rows = conn.execute(query)
scalar_record = rows.scalar()          # get the first row
print(scalar_record)

# we can use this syntax
# query = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')

"""
# When writing production code, you should follow these guidelines:
  - Use the first method for getting a single record over both the fetchone and scalar methods,
    because it is clearer to our fellow coders.
  - Use the iterable version of the ResultProxy over the fetchall and fetchone methods.
    It is more memory efficient and we tend to operate on the data one record at a time.
  - Avoid the fetchone method, as it leaves connections open if you are not careful.
  - Use the scalar method sparingly, as it raises errors if a query ever returns more than one row with one column,
    which often gets missed during testing.
"""

# -------------------------------------
# → Controlling the Columns in the Query
# --------------------------------------
print()
print('---- Controlin Columns in The Query ----')
query = select([cookies.c.cookie_name, cookies.c.quantity])
rows = conn.execute(query)
print(rows.keys())            # list of columns name
result = rows.first()
print(result)

# print result in table
from terminaltables import AsciiTable
table_data = [rows.keys()]                         # append description as table headers
table_data.append(result)
table_instance = AsciiTable(table_data)
print(table_instance.table)

# -------------------------------------
# → order_by: select().order_by()
# --------------------------------------
print()
print('----| order_by() |----')
query = select([cookies]).order_by(cookies.c.quantity)  # default order is ASC
rows = conn.execute(query)
for cookie in rows:
    print('{}'.format(cookie))

print()
print('----| order_by(desc(cookies.c.quantity)) |----')
from sqlalchemy import desc
query = select([cookies]).order_by(desc(cookies.c.quantity))        # DESC ordering
# query = select([cookies]).order_by(cookies.c.quantity.desc())     # Another Syntax
rows = conn.execute(query)
for cookie in rows:
    print('{}'.format(cookie))

# -------------------------------------
# → LIMT: select().limit()
# --------------------------------------
print()
print('---- select().limit() ----')
query = select([cookies.c.cookie_name, cookies.c.quantity]).order_by(cookies.c.quantity).limit(2)
rows = conn.execute(query)
print([row.cookie_name for row in rows])

# -------------------------------------
# → Built-In SQL Functions and Labels
# --------------------------------------

# SQLAlchemy can also laverage SQL functions found in the backend databas. Like SUM() and COUNT()
# To use these functions, we need to import the sqlalchemy.sql.func
from sqlalchemy.sql import func

print()
print('---- Built-in SQL Functions ----')
query = select([func.sum(cookies.c.quantity)])
rows = conn.execute(query)
print('- SUM Of All Quantity: {}'.format(rows.scalar()))      # scalar is usefull here, will return leftmost column in the first record.

query = select([func.count(cookies.c.cookie_name)])
rows = conn.execute(query)
rows = rows.first()
print('- COUNT: {}, value: {}'.format(rows.keys(), rows.count_1))
# The column name is autogenerated and is commonly func_name_position like here count_1

# alias
query = select([func.count(cookies.c.cookie_name).label('inventory_count')])        # set an alias with label
rows = conn.execute(query)
rows = rows.first()
print('- ALIAS AS : {}, value: {}'.format(rows.keys(), rows.inventory_count))

# -------------------------------------
# → Filtering: select().where()
# --------------------------------------

print()
print('---- select().where() ----')
query = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
rows = conn.execute(query)
rows = rows.first()
print(rows.items())     # items: return a list of columns and values

query = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))  # LIKE
rows = conn.execute(query)
for row in rows.fetchall():
    print(row.cookie_name)
"""
# ClauseElement methods

| Method                    | Purpose
|---------------------------|------------------------------------------------------
| between(cleft, cright)    | Find where the column is between cleft and cright
| concat(column_two)        | Concatenate column with column_two
| distinct()                | Find only unique values for the column
| in_([list])               | Find where the column is in the list
| is_(None)                 | Find where the column is None (commonly used for Null checks with None)
| contains(string)          | Find where the column has string in it (case-sensitive)
| endswith(string)          | Find where the column ends with string (case-sensitive)
| like(string)              | Find where the column is like string (case-sensitive)
| startswith(string)        | Find where the column begins with string (case-sensitive)
| ilike(string)             | Find where the column is like string (this is not case-sensitive)

* There are also negative versions of these methods, such as notlike and notin_().
  The only exception to the not<method> naming convention is the isnot() method, which drops the underscore.
"""

# Operator
print()
print('---- OPERATOR ----')
query = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])  # concat cookie_sku with SKU-
print(str(query))
for row in conn.execute(query):
    print(row)                      # ('chocolate chip', 'SKU-CC01')

from sqlalchemy import cast, Numeric
# Cast(): allows us to convert types. In the case, we will be getting back results as Numberic(12, 2)
print()
print('---- cast() ----')
query = select([cookies.c.cookie_name, cast((cookies.c.quantity * cookies.c.unit_cost), Numeric(12, 2)).label('inv_cost')])
for row in conn.execute(query):
    print('{} - {}'.format(row.cookie_name, row.inv_cost))

# Conjuctions in SQLAlchemy are and_(), or_(), and not_()
from sqlalchemy import and_, or_
print()
print('---- and_(), or_() ----')
print()
print('[+] and_()')
query = select([cookies]).where(and_(cookies.c.quantity > 23, cookies.c.unit_cost < 0.40))
for row in conn.execute(query):
    print(row)

print()
print('[+] or_()')
query = select([cookies]).where(or_(cookies.c.quantity.between(10, 50), cookies.c.cookie_name.contains('chip')))
for row in conn.execute(query):
    print(row)

"""
* The not_() function works in a similar fashion to other conjunctions,
  and it simply is used to select records where a record does not match the supplied clause.
"""
