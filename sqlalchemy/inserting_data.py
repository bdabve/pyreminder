#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : 2.inserting_data.py
#      CREATED : 11-November-2019
#       AUTHOR : daBve, dabve@outlook.fr
#
#         DESC : Inserting data with SQLAlchemy
#        USAGE : ./2.inserting_data.py
# ====================================================================================================

from sqlalchemy import create_engine
from sqlalchemy import insert
from create_tables import cookies, login, users, orders, line_items

engine = create_engine('sqlite:///sql_alchemy.sqlite')
conn = login(engine)

ins = cookies.insert().values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)

# print(str(ins))                     # Shows us the actual SQL statement that will be excuted.
# print(ins.compile().params)         # Actual parameters that will be sent with the query.
result = conn.execute(ins)          # Execute the query
print(result.inserted_primary_key)  # Inserted id

"""
# Insert as a top-level function.
from sqlalchemy import insert
ins = insert(cookies).values(       # table name as argument to the insert function
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)
"""

# values in execute statement
ins = cookies.insert()
result = conn.execute(
    ins,
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity='1',
    unit_cost='0.75'
)
print(result.inserted_primary_key)


# Multiple insert
inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.heml',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]
result = conn.execute(ins, inventory_list)
print(result.rowcount)

# inserting into users table
customer_list = [
    {
        'username': 'cookiemon',
        'email_address': 'mon@cookie.com',
        'phone': '111-111-1111',
        'password': 'password'
    },
    {
        'username': 'cakeeater',
        'email_address': 'cakeeater@cake.com',
        'phone': '222-222-2222',
        'password': 'password'
    },
    {
        'username': 'pieguy',
        'email_address': 'guy@pie.com',
        'phone': '333-333-3333',
        'password': 'password'
    }
]
query = users.insert()
rows = conn.execute(query, customer_list)
print('customers:', rows.rowcount, 'records inserted.')

# Enter order.
ins = insert(orders).values(user_id=1, order_id=1)
rows = conn.execute(ins)
print('order_items 1 :', rows.rowcount, 'records.')

line_items_list = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 2,
        'extended_cost': 1.00
    },
    {
        'order_id': 1,
        'cookie_id': 3,
        'quantity': 12,
        'extended_cost': 3.00
    }
]
query = insert(line_items)
rows = conn.execute(query, line_items_list)
print('line_items 1:', rows.rowcount, 'records.')
#
query = insert(orders).values(user_id=2, order_id=2)
rows = conn.execute(query)
print('order_items 2:', rows.rowcount, 'records inserted.')

line_items_list = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 24,
        'extended_cost': 12.00
    },
    {
        'order_id': 2,
        'cookie_id': 4,
        'quantity': 6,
        'extended_cost': 6.00
    }
]
query = insert(line_items)
rows = conn.execute(query, line_items_list)
print('line_items 2:', rows.rowcount, 'records inserted.')
