#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : join_tables.py
#      CREATED : 12-November-2019
#       AUTHOR : daBve, dabve@outlook.fr
#
#         DESC : join multiple tables, Grouping with SQLAlchemy
#        USAGE : ./join_tables.py
# ====================================================================================================

from sqlalchemy import create_engine
from create_tables import cookies, login, users, ordres, line_items
from sqlalchemy.sql import select

engine = create_engine('postgresql+psycopg2://dabve:sqlUbuntu@localhost:5432/dabve', pool_recycle=3600)
conn = login(engine)

columns = [ordres.c.order_id, users.c.username, users.c.phone,
           cookies.c.cookie_name, line_items.c.quantity,
           line_items.c.extended_cost]

cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(ordres.join(users).join(line_items).join(cookies)
                                                ).where(users.c.username == 'cookiemon')
rows = conn.execute(cookiemon_orders).fetchall()
for row in rows:
    print(row)

# Outer join
from sqlalchemy.sql import func
columns = [users.c.username, func.count(ordres.c.order_id)]
all_orders = select(columns).select_from(users.outerjoin(ordres)).group_by(users.c.username)
rows = conn.execute(all_orders).fetchall()
for row in rows:
    print(row)

# Grouping
print('---- Grouping ----')
columns = [users.c.username, func.count(ordres.c.order_id)]
all_orders = select(columns).select_from(users.outerjoin(ordres)).group_by(users.c.username)
rows = conn.execute(all_orders).fetchall()
for row in rows:
    print(row)


# Chaining
def get_orders_by_customer(cust_name, shipped=None, details=False):
    """Got a list of orders by customer"""
    columns = [ordres.c.order_id, users.c.username, users.c.phone]
    joins = users.join(ordres)
    if details:
        columns.extend([cookies.c.cookie_name, line_items.c.quantity, line_items.c.extended_cost])
        joins = joins.join(line_items).join(cookies)
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins)
    cust_orders = cust_orders.where(users.c.username == cust_name)
    if shipped is not None:
        cust_orders = cust_orders.where(ordres.c.shipped == shipped)
    rows = conn.execute(cust_orders).fetchall()
    return rows


print('---- With Function ----')
rows = get_orders_by_customer('cakeeater')
for row in rows:
    print(row)

rows = get_orders_by_customer('cakeeater', details=True)
for row in rows:
    print(row)

rows = get_orders_by_customer('cakeeater', shipped=True)
for row in rows:
    print(row)

rows = get_orders_by_customer('cakeeater', shipped=False)
for row in rows:
    print(row)

rows = get_orders_by_customer('cakeeater', shipped=False, details=True)
for row in rows:
    print(row)
